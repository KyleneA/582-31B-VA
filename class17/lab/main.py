from core.constants import MAX_TICKETS_PER_BOOKING
from core.enums import ShowStatus
from core.utils import Helper
from models.customer import Customer
from models.staff import Staff
from models.movie_show import MovieShow

def main():
    customer = Customer("Ava")
    staff = Staff("Sam")
    show = MovieShow("Inception", 20, ShowStatus.OPEN)
    max_tickets = f"Max tickets per booking:  {MAX_TICKETS_PER_BOOKING}"
    to_display = [customer, staff, show, max_tickets]

    Helper.displayHelper(to_display)

    # customer.display_info()
    # staff.display_info()
    # show.display_info()

if __name__ == "__main__":
    main()