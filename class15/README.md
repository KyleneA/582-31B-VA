# Advanced Programming — Project Exam

### Duration

3 hours

### Format

Individual, project-based, open IDE

---

# Objective

In this exam, you will design and implement a small Python application for a **Movie Ticket Booking System**.

Your code must be clear, organized, and executable.

---

# Scenario

A cinema wants a small internal system to manage movie shows and ticket bookings.

The system must support:

- different types of users
- movie shows with limited seat capacity
- booking operations with business rules
- protection against invalid object states
- clear exception handling when invalid actions are attempted

---

# General Requirements

Your solution must include all of the following:

- at least **one constant**
- at least **one enum**
- at least **one parent class**
- at least **two child classes**
- at least **one main business class**
- at least **two custom exceptions**
- use of **private attributes**
- use of **properties**
- enforcement of **invariants**
- use of **exception handling**
- a `main` section that demonstrates both valid and invalid operations

You **should** complete the exam in:

- multiple Python files

---

# Part 1 — Constant

Create the following constant:

```python
MAX_TICKETS_PER_BOOKING
```

You must use it meaningfully in your program.

For example:

- one customer cannot book more than this many tickets in a single booking operation

---

# Part 2 — Enum

Create an enum called:

```python
ShowStatus
```

It must contain these values:

- `OPEN`
- `SOLD_OUT`
- `CANCELLED`

Use this enum in your program instead of plain strings.

---

# Part 3 — Inheritance

Create a parent class called:

```python
User
```

## `User` requirements

### Attributes

- `name`
- `email`

### Method

- `display_info()`

---

Create **two child classes**:

- `Customer`
- `Staff`

## `Customer` requirements

### Additional private attribute

- `__customer_id`

### Behavior

- override `display_info()`

---

## `Staff` requirements

### Additional private attribute

- `__employee_id`

### Behavior

- override `display_info()`

---

# Part 4 — Main Business Class

Create a class called:

```python
MovieShow
```

This is the core business class of the exam.

## Required private attributes

- `__title`
- `__capacity`
- `__booked_seats`
- `__status`

---

## Required invariants

Your `MovieShow` class must enforce these rules:

- title cannot be empty
- capacity must be greater than 0
- booked seats cannot be negative
- booked seats cannot exceed capacity
- status must be a valid `ShowStatus`

---

## Required properties

Create properties for at least:

- `capacity`
- `status`

You may also create one for `booked_seats` if you wish.

Validation should happen through properties where appropriate.

---

## Required methods

### `book_tickets(customer, quantity)`

This method books tickets for a customer.

Rules:

- `quantity` must be greater than 0
- `quantity` must not exceed `MAX_TICKETS_PER_BOOKING`
- cannot book tickets if the show is cancelled
- cannot book tickets if the show is sold out
- cannot book more tickets than remaining seats

If booking succeeds:

- increase booked seats
- if the show becomes full, update the status to `SOLD_OUT`

---

### `cancel_show()`

This method changes the show status to `CANCELLED`.

---

### `display_info()`

This method displays information about the show, including:

- title
- capacity
- booked seats
- status

---

### Read-only computed property

Create a read-only property called:

```python
remaining_seats
```

It should return:

```python
capacity - booked_seats
```

---

# Part 5 — Custom Exceptions

Create at least **two custom exceptions**.

Suggested ideas:

- `InvalidBookingError`
- `ShowSoldOutError`

You may also define:

- `ShowCancelledError`
- `InvalidStatusError`

Use at least two custom exceptions meaningfully in your program.

## Example situations where exceptions may be raised

- invalid ticket quantity
- booking too many tickets
- booking a sold-out show
- booking a cancelled show
- invalid status assignment

---

# Part 6 — Encapsulation and Properties

Your solution must clearly demonstrate encapsulation.

This means:

- important state should use **private attributes**
- outside code should not directly manipulate internal state
- properties should provide controlled access
- your classes should protect themselves from invalid changes

---

# Part 7 — Polymorphism

Demonstrate polymorphism by placing different user objects in a list and calling the same method on each.

For example:

- one `Customer`
- one `Staff`

Then use a loop to call:

```python
display_info()
```

on each object.

---

# Part 8 — Exception Handling in `main`

In your `main` section, demonstrate both:

## Valid operations

Examples:

- create valid users
- create a valid movie show
- book valid tickets
- display updated information

## Invalid operations

Use `try/except` to demonstrate cases such as:

- booking too many tickets
- booking a sold-out show
- booking a cancelled show
- invalid capacity
- invalid status

Your program should show clear output for both success and failure cases.

# What Will Be Graded

Your work will be graded on:

- correct object-oriented design
- correct use of inheritance
- correct use of polymorphism
- correct use of private attributes
- correct use of properties
- correct enforcement of invariants
- meaningful use of enums and constants
- meaningful use of custom exceptions
- proper `try/except` handling in the demonstration code
- code correctness and clarity

---

# Optional Bonus

You may complete one or more of the following for bonus consideration:

## Bonus A

Add a method:

```python
reopen_show()
```

Rule:

- allowed only if the show is `SOLD_OUT`
- not allowed if the show is `CANCELLED`

---

## Bonus B

Add a read-only property:

```python
is_full
```

It should return `True` if `remaining_seats == 0`.

---

## Bonus C

Add a new child class:

```python
VIPCustomer
```

This class should inherit from `Customer`.

---

# Final Reminder

This is a **project exam**, so focus on:

- correctness
- clean structure
- meaningful use of course concepts

A smaller, correct, well-organized solution is better than a large incomplete one.
