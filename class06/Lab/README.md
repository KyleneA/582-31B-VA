# VCS Lab

In this lab, students practice version control while continuing to work with Python classes and methods. They will create a small class-based program, track their work with Git, use branches for separate features, and merge changes back into the main branch.

## Lab theme

Library Item Tracker

You will build a small Python program for tracking library items.

The program will use a class such as Book and will gradually add:

instance attributes
instance methods
a class attribute
a class method
a static method

Each major feature must be developed with Git commits and branches.

## Part 1 — Repository setup

### Task

Create a new project folder named in your lab folder:

```
library-item-tracker
```

Inside it, create:

```
book.py
main.py
.gitignore
```

Suggested `.gitignore`

```
__pycache__/
*.pyc
```

#### Git tasks

You must:

- commit everything

##### Expected commands

```
git add .
git commit -m "Initial project setup"
```

## Part 2 — Base implementation on main

### Programming task

Create a basic Book class in `book.py`.

### Requirements

The class must have instance attributes:

```
title
author
available
```

The constructor should initialize them.

In `main.py`

Students must:

- create at least 2 book objects
- print their attribute values

### Git task

Commit this base version.

## Part 3 — Feature branch 1: instance methods

### Git task

Create and switch to a new branch:

```
feature/instance-methods
```

Example commands

```
git checkout -b feature/instance-methods
```

### Programming task

Add instance methods to Book:

```
borrow()
return_book()
display_info()
```

#### Behavior

- `borrow()` should set available to False if possible
- `return_book()` should set available to True
- `display_info()` should print readable book information

In `main.py` Update the test code to call the methods.

### Git tasks

Make at least 2 commits on this branch. (As much as you want!)

- Example commit sequence
- Add display_info instance method
- Add borrow and return_book methods

## Part 4 — Feature branch 2: class and static methods

### Git task

Go back to main, then create a new branch:

feature/class-features

Example commands

```
git checkout main
git checkout -b feature/class-features
```

#### Programming task

Add the following to `Book`:

#### Class attribute

- `library_name = "Central Library"`

#### Class method

- `change_library_name(new_name)`

#### Static method

- `is_valid_title(title)`

In `main.py`

Test the class and static methods.

### Git tasks

Again, at least 2 commits on this branch are required.

## Part 5 — Merge the branches

Merge both branches back into main.

## Task

switch back to main

- merge feature/instance-methods
- merge feature/class-features

## Part 6 — Merge conflict exercise

You must now create and resolve a simple merge conflict.

#### Step 1 — change `display_info()` on main

Edit the `display_info()` method in `book.py` so it uses a different display format.

For example, change the way the output string is printed.

Commit the change on main.

#### Step 2 — create a new branch

Create a branch named:

`feature/display-style`

On this branch, change the same `display_info()` method again, but in a different way.

Commit the change.

#### Step 3 — merge and resolve conflict

Merge feature/display-style back into main.

If Git reports a conflict:

- open the file
- read the conflict markers
- decide which version to keep, or combine them
- remove the conflict markers
- save the file
- add the resolved file
- complete the merge commit

## Final Program Requirements

By the end of the lab, your Book class must include:

#### Instance attributes

- title
- author
- available

#### Instance methods

- borrow()
- return_book()
- display_info()

#### Class attribute

- library_name

#### Class method

- change_library_name(new_name)

#### Static method

- is_valid_title(title)

## Final main.py Requirements

Your main.py should demonstrate:

- creating book objects
- borrowing and returning books
- displaying book information
- changing the library name
- validating at least two different titles

## Challenge Tasks

### Challenge 1 — Add a class counter

Add a class attribute:

`count = 0`

Increment it in the constructor.

Add a class method:

`show_count()`

Test it in main.py.

### Challenge 2 — Add an alternative constructor

Add a class method:

- `from_string(data)`

Use input like:

"Clean Code,Robert C. Martin,True"

This method should parse the string and return a Book object.

### Challenge 3 — Add a genre feature branch

Create a new branch:

`feature/genre`

Add:

- a genre attribute
- support for genre in the constructor
- genre in display_info()

Then merge the branch back into main.

### Challenge 4 — Show your Git history

Run:

```
git log --oneline --graph --all
```

## Commands You Will Probably Need

- Initialize repository

```
git init
```

- Check status

```
git status
```

- Stage files

```
git add .
```

- Commit

```
git commit -m "Your message here"
```

- Create and switch branch

```
git checkout -b branch-name
```

- Switch branch

```
git checkout main
```

- Merge branch

```
git merge branch-name
```

- View branches

```
git branch
```

- View history

```
git log --oneline --graph --all
```

## Optional Starter Template

- `book.py`

```
class Book:
    pass
```

- `main.py`

```
from book import Book

# create and test your objects here
```
