from flask import (Flask, render_template, request, redirect, url_for)
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bike.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Station(db.Model):
    __tablename__ = "station"

    id = db.Column(
        db.Integer, 
        primary_key = True
    )

    name = db.Column(
        db.String(120), 
        nullable=False
    )

    capacity = db.Column(
        db.Integer, 
        nullable=False
    )

    bikes = db.relationship(
        "Bike", 
        back_populates="station"
    )

    # DOMAIN LOGIC

    @property
    def bike_count(self):
        return len(self.bikes)
    
    @property
    def available_bike_count(self):
        sum = 0

        for bike in self.bikes:
            if bike.can_be_rented:
                sum +=1
        
        return sum
    
    @property
    def remaining_capacity(self):
        return self.capacity - self.bike_count

    @property
    def has_space(self):
        return self.remaining_capacity > 0

    def add_bike(self, bike):
        if not self.has_space:
            return False

        self.bikes.append(bike)
        return True

    def __repr__(self):
        return f"<Station {self.id}: {self.name}>"


class Bike(db.Model):
    __tablename__ = "bike"

    id = db.Column(
        db.Integer, 
        primary_key = True
    )

    is_available = db.Column(
        db.Boolean, 
        nullable = False, 
        default = True
    )

    bike_type = db.Column(
        db.String(20), 
        nullable = False
    )

    distance_km = db.Column(
        db.Float, 
        nullable = False, 
        default = 0
    )

    station_id = db.Column(
        db.Integer, 
        db.ForeignKey("station.id"), 
        nullable = False
    )

    # in relationship first argument is the Python model name, then back_populates is the name of the table
    station = db.relationship("Station", 
        back_populates="bikes")

    @property
    def need_service(self):
        return self.distance_km >= 1000

    @property
    def can_be_rented(self):
        return (self.is_available and not self.need_service)

    def rent_bike(self):
        if not self.can_be_rented:
            return False
        
        self.is_available = False
        return True
    
    def return_bike(self):
        self.is_available = True

    def record_ride(self, distance):
        # returning boolean for API status to be able to do try/catch
        if distance <= 0:
            return False 
        
        self.distance_km += distance
        return True

    def __repr__(self):
        return (
            f"<Bike {self.id}: {self.bike_type}"
        )

with app.app_context():
    db.create_all()

    # # Creating objects
    # downtown_station = Station(
    #     name = "Downtown Station",
    #     capacity = 4
    # )


    # bike_100 = Bike(
    #     bike_type = "Standard",
    #     is_available = True,
    #     distance_km = 200
    # )

    # bike_101 = Bike(
    #     bike_type = "Electric",
    #     is_available = True,
    #     distance_km = 800
    # )

    # #connecting bike to station
    # downtown_station.bikes.append(bike_100)
    # bike_101.station = downtown_station

    # db.session.add(downtown_station)
    # db.session.commit()

    # db.session.add(bike_100)
    # db.session.add(bike_101)

    # db.session.commit()
    
    # print(downtown_station)
    # print(bike_100)
    # print(bike_101)

    @app.route("/")
    def home():
        return redirect(url_for("stations"))

    @app.route("/stations")
    def stations():
        all_stations = Station.query.all()
        
        return render_template("stations.html", stations=all_stations)
    
    @app.route("/stations/<int:station_id>")
    def station_detail(station_id):
        station = Station.query.get_or_404(station_id)

        return render_template("station_detail.html", station=station)

    @app.route("/bikes/<int:bike_id>/rent", methods=["POST"])
    def rent_bike(bike_id):
        bike = Bike.query.get_or_404(bike_id)

        if bike.rent_bike():
            db.session.commit()

        return redirect(url_for("station_detail", station_id=bike.station_id))

    @app.route("/bikes/<int:bike_id>/return", methods=["POST"])
    def return_bike(bike_id):
        bike = Bike.query.get_or_404(bike_id)

        bike.return_bike()
        db.session.commit()

        return redirect(url_for("station_detail", station_id=bike.station_id))

    @app.route("/bikes/add", methods=["GET","POST"])
    def add_bike():
        stations = Station.query.all()

        if request.method == "POST":
            station_id = int(request.form["station_id"])

            station = Station.query.get_or_404(station_id)

            bike = Bike(
                bike_type=request.form["bike_type"],
                distance_km=float(request.form["distance_km"]),
                is_available=True
            )

            # Checking if station is full
            if not station.add_bike(bike):
                return render_template(
                    "add_bike.html",
                    stations=stations,
                    error="The selected station is full"
                )
            
            db.session.add(bike)
            db.session.commit()

            return redirect(url_for("station_detail", station_id=station.id))
        
        return render_template("add_bike.html", stations=stations)