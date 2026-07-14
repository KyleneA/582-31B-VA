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
3. In the album database model, the year was set to a string even though the requirements state that it should be an integer.
4. The **in_stock** property should return `self.stock > 0`
5. The app context was missing parentheses `with app.app_context:`

**Fix:**  
1. I added the argument for the app to line 17
2. I updated the database address to `SQALCHEMY_DATABASE_URI` in line 14
3. I changed the type to integer in line 42
4. I changed the operator to larger than to ensure **in_stock** returns true when there is stock in line 54
5. I added the missing parentheses in line 60


**Test:**  
I ran the command `flask --app app run --debug` to check that I received no errors.

-----
-----

## Bug title

**File:**  
Name of the file.

**Problem:**  
What was incorrect?

**Fix:**  
What did you change?

**Test:**  
How did you confirm that it worked?

-----
-----

## Bug title

**File:**  
Name of the file.

**Problem:**  
What was incorrect?

**Fix:**  
What did you change?

**Test:**  
How did you confirm that it worked?

-----
-----

## Bug title

**File:**  
Name of the file.

**Problem:**  
What was incorrect?

**Fix:**  
What did you change?

**Test:**  
How did you confirm that it worked?

-----
-----

## Bug title

**File:**  
Name of the file.

**Problem:**  
What was incorrect?

**Fix:**  
What did you change?

**Test:**  
How did you confirm that it worked?