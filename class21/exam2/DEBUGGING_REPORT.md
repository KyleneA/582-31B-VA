> [!Requirements]
> At least one example must come from each of these categories:
>
> - Python or model code
> - Flask route
> - database operation
> - template or form
> - logic error
>

-----
-----

## Flask-SQLAlchemy configuration errors

**File:**  
`app.py`

**Problem:**  
1. The database initialization was missing the argument to the project app
2. The address to the database should be "SQALCHEMY_DATABASE_URI" but it was "URL".
3. The app context was missing parentheses `with app.app_context:`

**Fix:**  
1. I added the argument for the app to line 17
2. I updated the database address to `SQALCHEMY_DATABASE_URI` in line 14
3. I added the missing parentheses in line 60


**Test:**  
I ran the command `flask --app app run --debug` to check that I received no errors.

-----
-----

## Routing errors

**File:**  
`base.html`

**Problem:**  
anchor link for navigation bar in `base.html` refers to *albums* and *add* (routing methods that don't exist) instead of **index** and **add_album**

**Fix:**  
I updated the routing method names to ensure 

**Test:**  
I refreshed the page to see if the build error disappeared

-----
-----

## Database operation errors

**File:**  
`app.py`

**Problem:**  
1. The code adding the album to the database was missing when creating the "albums/add" route
2. The code to commit database session changes was missing for the edit_album and delete_album routing methods.

**Fix:**  
1. I added `db.session.add(album)` to line 96 prior to the code commiting the changes to the database
2. I added the `db.sesion.commit()` to each if the routing methods

**Test:**  
1. I tried adding an album to see if the album card would be created in the home page.
2. I tried editing and deleting an album to see if the changes were saved.

-----
-----

## FORM or Template error

**File:**  
`add_album.html`

**Problem:**  
The form method was GET instead of POST

**Fix:**  
I changed the form method to POST

**Test:**  
Tried adding an album to see if it was added to the database.

-----
-----

## Logic Error

**File:**  
`app.py`

**Problem:**  
1. The **in_stock** property was set to return "self.stock < (smaller than) 0"
2. The edit_album routing method used "add_album.html" for the template file instead of "edit_album.html"

**Fix:**  
1. I changed the operator to ">" (larger than)
2. I corrected the template file name to "edit_album.html"
3. The redirect after editing the album was the edit page instead of the home page

**Test:**  
1. I tried adding an album with stock set to 0
2. I clicked on the edit button from the homepage to see which template was rendered when I clicked the button
3. I changed the url_for() contents to "index"