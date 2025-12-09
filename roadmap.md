# **📅 Day 1 — Introduction to Django & Setup**

### **Topics**

* What is Django? MVT architecture
* Request/response flow
* How Django handles URLs → Views → Templates
* Install Python, pip, venv
* Install Django
* Start first Django project (`django-admin startproject`)
* Project structure (`manage.py`, settings, wsgi, urls)

### **Tasks**

* Install Django
* Follow this tutorial https://docs.djangoproject.com/en/6.0/intro/tutorial01/
---

# **📅 Day 2 — Django Apps & Project Structure**

### **Topics**

* What is an app?
* `startapp` command
* App structure: models, views, urls
* Registering apps in `INSTALLED_APPS`
* Django settings deep dive

### **Tasks**

* Create an app: `accounts`
* Add its URLs into project URLs
* Create basic view returning HttpResponse

---

# **📅 Day 3 — URL Routing & Views**

### **Topics**

* URL patterns
* Path converters (`int`, `slug`, `uuid`)
* Function-based views (FBV)
* HttpResponse, JsonResponse
* Request object basics

### **Tasks**

* Build 5 URLs with dynamic values
* Show values captured from URL in views
* Return HTML, JSON from views

---

# **📅 Day 4 — Templates & Rendering**

### **Topics**

* Templates folder structure
* Django template language
* Variables, loops, conditions
* Template inheritance (`extends`, `block`)
* Includes

### **Tasks**

* Create base.html
* Create two child pages
* Add navigation bar via `include`
* Render dynamic data in templates

---

# **📅 Day 5 — Static & Media Files**

### **Topics**

* `STATIC_URL`, `STATICFILES_DIRS`, `collectstatic`
* Serving media files
* Uploading images (basic)

### **Tasks**

* Add CSS & JS static files
* Add images
* Create a page with custom CSS
* Upload an image & display it

---

# **📅 Day 6 — Django Models & ORM Basics**

### **Topics**

* Creating models
* Fields (CharField, IntegerField, DateField, etc.)
* Migrations (`makemigrations`, `migrate`)
* ORM basics: `all()`, `get()`, `filter()`
* Django shell

### **Tasks**

* Create a `Book` model
* Run migrations
* Add sample rows via shell
* Query & filter them

---

# **📅 Day 7 — Model Relationships**

### **Topics**

* One-to-many (ForeignKey)
* Many-to-many
* One-to-one
* Related_name
* Cascading deletes

### **Tasks**

* Create models: Author → Books
* Create models: Students ↔ Courses
* Query relational data in shell

---

# **📅 Day 8 — Django Admin Mastery**

### **Topics**

* Registering models
* Customizing admin list & detail views
* Search fields, list filters
* Inline models
* Custom admin actions

### **Tasks**

* Register all models
* Add filtering & search
* Add inline books under authors

---

# **📅 Day 9 — Forms & Working With POST Data**

### **Topics**

* HTML forms
* Django form class
* CSRF token
* `request.POST`
* GET vs POST

### **Tasks**

* Create a form to add a new Book
* Validate form input
* Save to database

---

# **📅 Day 10 — Django ModelForms**

### **Topics**

* ModelForm structure
* Auto-generated form fields
* Form validation
* Custom validators
* Clean methods

### **Tasks**

* Create ModelForm for Book
* Add custom validation (min length)
* Display form errors in template

---

# **📅 Day 11 — Class-Based Views (CBV)**

### **Topics**

* Why CBV?
* TemplateView, ListView, DetailView
* CreateView, UpdateView, DeleteView
* Understanding dispatch()
* Overriding class methods

### **Tasks**

* Convert Book CRUD to CBVs
* Override a method (e.g. form_valid)

---

# **📅 Day 12 — Messaging Framework & Redirects**

### **Topics**

* `messages` framework
* Success, error messages
* Redirects with `reverse` & `redirect`
* `next` parameter

### **Tasks**

* Show message when new Book is added
* Redirect users after update/delete

---

# **📅 Day 13 — Authentication System (Part 1)**

### **Topics**

* Django auth system
* User model basics
* Login & logout views
* Password hashing
* User creation

### **Tasks**

* Create login page
* Create logout page
* Restrict a page to logged-in users

---

# **📅 Day 14 — Authentication System (Part 2)**

### **Topics**

* User registration
* Password reset (email backend)
* Customizing user fields
* LoginRequiredMixin
* PermissionsRequiredMixin

### **Tasks**

* Create signup page
* Add password reset flow
* Add protected views using mixins

---

# **📅 Day 15 — Custom User Model**

### **Topics**

* Why custom user model?
* AbstractUser vs AbstractBaseUser
* Creating custom user model from scratch
* Update admin panel to support new model

### **Tasks**

* Replace default user with custom user model
* Add phone number field
* Test login/signup

---

# **📅 Day 16 — Advanced ORM & Query Optimization**

### **Topics**

* `select_related` & `prefetch_related`
* Aggregations (Count, Sum, Avg)
* Q objects
* F expressions
* Annotate
* Raw SQL

### **Tasks**

* Show number of books per author in a list
* Write query using Q filters
* Optimize N+1 queries

---

# **📅 Day 17 — Middleware**

### **Topics**

* What is middleware?
* Order of middleware execution
* Custom middleware
* Request/response modification
* Logging middleware

### **Tasks**

* Create middleware that logs user IP
* Create middleware that blocks certain paths

---

# **📅 Day 18 — Signals**

### **Topics**

* Signal types: pre_save, post_save, post_delete
* Connect & disconnect signals
* Use cases:

  * Auto-creating profile
  * Logging
  * Updating counters

### **Tasks**

* Create signal that creates `Profile` after User creation
* Create signal that logs when Book is deleted

---

# **📅 Day 19 — File Uploads & Image Handling**

### **Topics**

* FileField / ImageField
* Handling uploads
* Validating image types
* Pillow library
* Serving uploaded files

### **Tasks**

* Add book cover upload feature
* Validate file size
* Display uploaded images

---

# **📅 Day 20 — Project Structuring, Best Practices & Deployment Prep**

### **Topics**

* Settings splitting (dev/prod)
* Using `.env`
* Template organization
* Staticfiles strategy
* App architecture best practices
* Clean code + folder structures
* Common pitfalls
* Deployment checklist (basic)

### **Tasks**

* Split settings into `base.py`, `dev.py`, `prod.py`
* Add environment variables
* Organize templates per app
* Create a small final CRUD project demonstrating all features

---

# 🎉 **Final Project**

**Instagram App**
