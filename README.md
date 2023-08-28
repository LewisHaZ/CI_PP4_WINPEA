# ** Winpea World - Jewellery Store ** 
 
![Am I Responsive](docs/am-i-responsive.png)
Developer: **Lewis Hazelwood**

Deployed Site:
[Winpea world - site](https://winpea-world-560ce7552450.herokuapp.com/)


## Table of Contents
  - [About](#about)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Colours](#colours)
    - [Fonts](#fonts)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [Database](#database)
    - [Wireframes](#wireframes)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [Automated testing](#automated-testing)
    - [Tests on various devices](#tests-on-various-devices)
    - [Browser compatibility](#browser-compatibility)
  - [Bugs](#bugs)
  - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

### About 

Winpea World is a Jewellery brand and store based in Leeds, England (UK). People who are interested in visiting and purchasing products can create an account, book a slot, read through blog posts and view the product catalogue.
<hr>

## Project Goals

### User Goals
- To create a slot (booking/reservation) for visitng the store
- To be able to view, edit and cancel slots
- To view a catalogue of products
- To be able to contact the business
- To be able to view a blog

### Site Owner Goals
- To attract customers to the store and sell products
- Fully responsive website and ease of access
- Provide a way to book a slot online without need for a phone call.
- Increased online presence in order to boost sales.
<hr>

## User Experience

### Target Audience
- People who are looking to purchase gifts for their family or friends.
- Past and new customers to our business.
- Tourists to the Leeds area who are shopping around.
- People looking to purchase anniversary gifts.
- Companies/anyone looking to host celebration parties in-store.

### User Requirments and Expectations
- Fully responsive
- Accessibility
- Clear and easy to read webpage
- Social Media
- Contact Information

##### Back to [top](#table-of-contents)<hr>

## User Stories

### Users
1. As a User I can navigate across the site so that I can move to each feature of the site easily (Must have)
2. As a User I can view the opening hours and contact details so that I know when the business is open and how to contact them via email, phone and socials (Must have)
3. As a Site Owner I can provide a contact us page so that users can get in touch with my business (Must have)
4. As a User I can use a navbar, footer, and social icons so that I can navigate the site, access menus, and access socials (Must have)
5. As a User I can create a booking by selecting a date and time so that I can reserve my slot (Must have) 
6. As a User I can update my booking so that I can choose another available time and date (Must have)
7. As a User I can delete my booking so that I can cancel my slot (Must have)
8. As a user I can view my booking so that I can remind myself of the date and time I have booked (Must have)
9. As a User I can I am notified so that I know my action of creation, edit, or deletion of a booking has been successful (Must have)
10. As a User I can register as prompted so that I can make a booking if I wish reserve a slot (Must have)
11. As a User I can register to create an account so that my details are stored for faster booking in future (Must have)
12. As a user I can login so that I can book a slot (Must have)
13. As a user I can see my login status so that I know if I am logged in or not (Must have)
14. As a User I can view the site's blog so that I can learn additional information and read articles (Should have)
15. As a User I can view the product catalogue so that I can decide whether to visit the store (Must have)
16. As a User I cannot book a date in the past so that my booking is valid (Must have)
17. As a User I can view blog posts page by page so that I can browse without seeing an overloaded page (Should have)
18. As a User I can not book a slot already booked so that my booking is valid and not double booked (Must have)

### Admin/Authorised Users
19. As an Admin / Authorised User I can log in so that I can access the back end of the site (Must have)
20. As an Admin / Authorised User I can manually add a booking so that I can book a slot if someone phones, or emails the business (Should have)
21. As an Admin / Authorised User I can accept or reject bookings so that we avoid double bookings (Must have)
22. As an Admin I can login to add or remove items from the product catalogue so that we can add more products or remove them (Must have)
23. As a Admin I can create, read, update and delete product item from the database so that we can add, remove, rename and view all our catalogue products (Must have)
24. As an Admin / Authorised User I can search through bookings and menus so that I can find the information I am looking for	 (Should have)
25. As an Admin / Authorised User I can filter bookings by date so that I can see what bookings we have for a particular day (Should have)

### Site Owner
26. As a Site Owner I can provide a fully responsive site for my customers so that they have a good user experience (Must have)
27. As a Site Owner I can validate data entered into my site so that all submitted data is correct to avoid errors (Must have)

# Epics & Kanbans 
- Epics have been used to track chunks of issues categorised into milestones.
- GitHub Kanban was used to track all open user stories.
- Todo, In progress and Done were used to track all issues in the Kanban

<details><summary>Kanban</summary>

![Kanban complete](https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/features/kanban-complete.png)

</details>

<details><summary>Epics</summary>

![Epics](https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/features/kanban-epics.png)
![Epic 1](https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/features/kanban-epics-1.png)
![Epic 2](https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/features/kanban-epics-2.png)
![Epic 3](https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/features/kanban-epics-3.png)
![Epic 4](https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/features/kanban-epics-4.png)

</details>

<details><summary>User Stories</summary>

![User stories](https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/features/user-stories.png)

</details>

##### Back to [top](#table-of-contents)<hr>

## Design

### Colours

The Winpea brand is a black and white design so for the site I kept with the brighter but simple feel to the sites design.
Upon doing some market research on other brands I was able to discern that simple colour palettes are usually favoured in
the design of Fashion websites.

Colours used include white, grey, black and a light/darker shade of blues for the footer.

### Fonts

Fonts were taken from Google Fonts; I used Playfair Display with sans serif as a backup.

### Structure

#### Website pages

The site has been designed in a way that the user will easily be able to access any page with a navbar at the top to navigate and hamburger menu for
small screen users.

The footer contains links to social media such as an Instagram page which has relevant content on the Winpea brand, this can in turn expand the customer base and boost sales
as it can easily be shared.

- The site consists of the following pages:
  - Homepage with cards for the user to choose to book a slot, view the community blog or our product catalogue
  - Catalogue has a list of all available and unavailable products from the database sorted by bags, necklaces, bracelets, earrings and new.
  - Blog page has a paginated list of blogs posted by an admin or authorised user, 4 per page
  - Blog expanded displays a blog the user has selected so they can read the blog, if they are logged in they can also leave a comment which will then need to be approved before it is displayed
  - Book page allows registered users to book a slot , change guest count, date requested, time requested and a product of interest to notify staff.
  - My bookings displays all bookings for the user that they have made, bookings in the past are automatically expired
  - Edit booking allows the user to change their date, time, product of interest and guest count
  - Cancel booking allows the user to cancel the booking which will then delete it from the database
  - Contact us allows the user to send us a message if the are registered, or they can contact us from the displayed email and phone number or visit the address listed.
  - Login / Logout allows users to login to make bookings, view, edit, and delete bookings
  - Register allows the user to register so they can use the booking system
  - 404 error page to display if a 404 error is raised

#### Database

- Built with Python and the Django framework with a database of a Postgres for the deployed Heroku version(production)
- Two database model shows all the fields stored in the database

<details><summary>Show diagram</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/database-schema.png">
</details>

##### User Model
The User Model contains the following:
- user_id
- password
- last_login
- is_superuser
- username
- first_name
- last_name
- email
- is_staff
- is_active
- is_banned
- date_joined

#### ProductItem Model
The ProductItem Model contains the following:
- item_id
- item_name
- item_image
- price
- available

#### Slot Model
The Slot Model contains the following:
- slot_id
- max_slots
- available

#### Booking Model
The Booking Model contains the following:
- booking_id (PrimaryKey)
- created_date
- requested_date
- requested_time
- slot (ForeignKey)
- customer (ForeignKey)
- status
- customer_count

#### Post Model (Blog)
- title
- post_id (PrimaryKey)
- author (ForeignKey)
- created_date
- updated_date
- content
- featured_image
- excerpt
- slug
- status

#### Comment Model (Blog)
- post (ForeignKey)
- name
- email
- body
- created_date
- approved
- Meta: created_on


##### ContactUs Model
The ContactUs Model contains the following:
- contact_id (PrimaryKey)
- name (ForeignKey)
- email (ForeignKey)
- phone (ForeignKey)
- body


### Wireframes
The wireframes were created using Balsamiq
<details><summary></summary>
<img src="docs/wireframes.png">
</details>


## Technologies Used

### Languages & Frameworks
- [Python](https://www.python.org/)
- [Javascript](https://www.javascript.com/)
- [HTML](https://www.w3.org/)
- [CSS](https://www.w3.org/)
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com//)


### Tools

- [Balsamiq](https://balsamiq.com/)
- [Cloudinary](https://cloudinary.com/)
- [Favicon.io](https://favicon.io)
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/)
- [Font Awesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/)
- [Heroku Platform](https://id.heroku.com/login)
- [jQuery](https://jquery.com)
- [Postgres](https://www.postgresql.org/)
- [Summernote](https://summernote.org/)
- [Git](https://git-scm.com/)
- [GitPod](https://gitpod.io/)
- [GitHub](https://github.com/)
- Validation:
  - [WC3 Validator](https://validator.w3.org/)
  - [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)
  - [JShint](https://jshint.com/)
  - [Pycodestyle(PEP8)](https://pypi.org/project/pycodestyle/)
  - [Lighthouse](https://developers.google.com/web/tools/lighthouse/)
  - [Wave Validator](https://wave.webaim.org/)


##### Back to [top](#table-of-contents)


## Features

### Home Page
- Home page includes nav bar, main body and a footer.

<details><summary>See feature images</summary>

![Home page](docs/features/features-homepage.jpg)
</details> 

### Logo & Navigation
- Custom logo for the business
- Fully Responsive
- On small screens switches to hamburger menu
- Indicates login/logout in status
- Displayed on all pages

<details><summary>See feature images</summary>

![nav](docs/features/features-navbar.png)
![nav](docs/features/features-navbar-login.png)
![nav](docs/features/features-navbar-small.png)
</details>

### Footer
- Contains social media links and copyright
- displayed across all pages

<details><summary>See feature images</summary>

![Footer](docs/features/features-footer.png)
</details>

### Sign up / Register
- Allow users to register an acoount
- Username and password is required, email is optional

<details><summary>See feature images</summary>

![Register](docs/features/features-register.png)
</details>

### Login
- User can login to create a booking, view bookings, edit and delete bookings
- User is prompted if they are not entering correct user login details

<details><summary>See feature images</summary>

![Login](docs/features/features-login.png)
![Login](docs/features/features-login-incorrect.png)
</details>

### Logout
- Allows the user to securely log out
- Ask user if they are sure they want to log out

<details><summary>See feature images</summary>

![Logout](docs/features/features-logout.png)
</details>

### Book
- Allows the user to book a slot using the booking form
- Messages are displayed if the data is not valid such as phone number lenght is too short and the email address is not a valid format
- Users can see when their booking is successful

<details><summary>See feature images</summary>

![Book](docs/features/features-booking-slot.png)
![Book](docs/features/features-booking-slot-valid.png)
![Book](docs/features/features-booking-slot-double.png)
![Book](docs/features/features-booking-slot-valid.png)
</details>

### My Bookings
- Allows the user to see all their bookings in a paginated layout, 4 per page
- If the booking is older than today it is automatically expired for the user
- Status of the booking is displayed, awaiting confirmation and when approved will then change to confirmed status for the user

<details><summary>See feature images</summary>

![My Bookings](docs/features/features-my-bookings.png)
</details>


### Edit Booking
- Allows the user to edit their booking to another date, time, guest count and slot
<details><summary>See feature images</summary>

![Edit Booking](docs/features/features-edit-booking.png)
</details>


### Cancel Booking 
- Allows the user to cancel their booking, asks user are they sure
  
<details><summary>See feature images</summary>

![Cancel Booking](docs/features/features-booking-cancel.png)
</details>

### Catalogue
- The catalogue displays all available and out of stock products
- Catalogue is categorised into each type of producet
- Items can be added via the admin panel in the backend by staff
- Staff can create, update and delete products via the admin panel
  
<details><summary>See feature images</summary>

![Catalogue](docs/features/features-catalogue.png)
</details>

### Blog
- The blog displays each post made by a staff member
- Paginations is used to display 4 posts per page
  
<details><summary>See feature images</summary>

![Blog](docs/features/features-blog.png)
</details>

### Blog Expanded
- Expands into the selected blog the user wishes to read
- Displays a featured image uploaded by the poster
- If no image is uploaded a default image is then used
- Registered user can comment on the blog
  
<details><summary>See feature images</summary>

![Blog Expanded](docs/features/features-blog-2-1.jpg)
</details>

### Comments
- Comments made are set to pending approval status to ensure nothing explicit is displayed
- Only registered users can comment on a blog post
- Staff can approve comments via the admin panel on the backend
  
<details><summary>See feature images</summary>

![Comments](docs/features/features-blog-comment.png)
</details>

### Contact Us
- Registered users can DM staff via the message box
- Contact info such as, phone, email, and address is displayed
- A Google Map is embedded with the address for users to use
  
<details><summary>See feature images</summary>

![Contact Us](docs/features/features-contactus.png)
</details>

### Social Media Links
- A logo and link is used for each social media displayed
- All links open in a new tab to ensure user is not directed away from the business
- Displayed on all pages
  
<details><summary>See feature images</summary>

![Social Media Links](docs/features/features-social-links.png)
</details>

### Pagination
- Pagination is used on the bookings list and the blog page
- Ensures the page is kept tidy as only 4 items are displayed per page
  
<details><summary>See feature images</summary>

![Pagination](docs/features/features-page-pagination.png)
</details>

##### Back to [top](#table-of-contents)<hr>

## Validation
### HTML Validation
The W3C Markup Validation Service was used to validate the HTML code for the webiste. All pages have passed the checks and have no errors - this can be checked at any time.
- Home [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwinpea-world-560ce7552450.herokuapp.com%2F)
- Register [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwinpea-world-560ce7552450.herokuapp.com%2Faccounts%2Fsignup%2F)
- Login [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwinpea-world-560ce7552450.herokuapp.com%2Faccounts%2Flogin%2F)
- Logout [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwinpea-world-560ce7552450.herokuapp.com%2Faccounts%2Flogout%2F)
- Bookings [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwinpea-world-560ce7552450.herokuapp.com%2Fvisit_store)
- Edit Booking [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwinpea-world-560ce7552450.herokuapp.com%2Fedit_booking%2F15)
- Cancel Booking [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwinpea-world-560ce7552450.herokuapp.com%2Fcancel_booking%2F15)
- Catalogue [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwinpea-world-560ce7552450.herokuapp.com%2Fcatalogue)
- Blog [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwinpea-world-560ce7552450.herokuapp.com%2Fblog%2F)
- Blog Expanded [results](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fwinpea-world-560ce7552450.herokuapp.com%2Fthe-timeless-influence%2F)
- Contact us [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwinpea-world-560ce7552450.herokuapp.com%2Fcontactus%2F)
- 404 page [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwinpea-world-560ce7552450.herokuapp.com%2Fvisit_stores%2F) - 404 is detected

### CSS Validation
The W3C Jigsaw CSS Validation Service
<details><summary>style.css</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/css-validaiton.png">
</details><hr>

### JS Validation
JSLint: The JavaScript Code Quality Coverage Tool
<details><summary>script.js</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/js-validaiton.png">
</details><hr>

### PEP8 Validation
Code Institute's CI Python Linter was used to validate all Python files.

<hr><summary>Home</summary><hr>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-urls-home.png">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-views-home.png">
</details>

<hr><summary>Item Catalogue</summary><hr>

<details><summary>admin.py</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-admin-catalogue.png">
</details>

<details><summary>models.py</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-models-catalogue.png">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-urls-catalogue.png">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-views-catalogue.png">
</details>

<details><summary>test-urls.py</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-test-urls-catalogue.png">
</details>

<details><summary>test-views.py</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-test-views-catalogue.png">
</details>

<hr><summary>Bookings</summary><hr>

<details><summary>admin.py</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-admin-booking.png">
</details>

<details><summary>models.py</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-models-booking.png">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-urls-booking.png">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-views-booking.png">
</details>

<details><summary>test-urls.py</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-test-urls-booking.png">
</details>

<details><summary>forms.py</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-forms-booking.png">
</details>

<details><summary>test-views.py</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-test-views-booking.png">
</details>

<hr><summary>Blog</summary><hr>

<details><summary>admin.py</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-admin-blog.png">
</details>

<details><summary>models.py</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-models-blog.png">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-urls-blog.png">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-views-blog.png">
</details>

<details><summary>forms.py</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-forms-blog.png">
</details>

<hr><summary>Contact us</summary><hr>

<details><summary>admin.py</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-admin-contactus.png">
</details>

<details><summary>models.py</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-models-contactus.png">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-urls-contactus.png">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-views-contacus.png">
</details>

<details><summary>forms.py</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-forms-contactus.png">
</details>

### Lighthouse

Performance of the site, best practices and SEO tested.


### Desktop
<details><summary>Index</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-lighthouse-desktop-home.png">
</details>

<details><summary>Register</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-lighthouse-desktop-regsiter.png">
</details>

<details><summary>Login</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-lighthouse-desktop-login.png">
</details>

<details><summary>Logout</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-lighthouse-desktop-logout.png">
</details>

<details><summary>Catalogue</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-lighthouse-desktop-catalogue.png">
</details>

<details><summary>Blog</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-lighthouse-desktop-blog.png">
</details>

<details><summary>Blog Expanded</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-lighthouse-desktop-blog=expanded.png">
</details>

<details><summary>Book</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-lighthouse-desktop-book.png">
</details>

<details><summary>Booking List</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-lighthouse-desktop-booking-list.png">
</details>

<details><summary>Edit Booking</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-lighthouse-desktop-edit-booking.png">
</details>

<details><summary>Cancel Booking</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-lighthouse-desktop-cancel-booking.png">
</details>

<details><summary>Contact Us</summary>
<img src="https://raw.githubusercontent.com/LewisHaZ/CI_PP4_WINPEA/main/docs/validation/validation-lighthouse-desktop-contactus.png">
</details>

#### Mobile

<details><summary>Index</summary>


<details><summary>Register</summary>


<details><summary>Login</summary>


<details><summary>Logout</summary>


<details><summary>Catalogue</summary>


<details><summary>Blog</summary>


<details><summary>Blog Expanded</summary>


<details><summary>Book</summary>


<details><summary>Booking List</summary>


<details><summary>Edit Booking</summary>


<details><summary>Cancel Booking</summary>


<details><summary>Contact Us</summary>

## Testing


* 
* 
* 
* 
* 


### Manual Testing

<details><summary>View manual testing</summary>

### Testing User Stories

 User:
1. As a User, I would like to...

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|||||
|Navbar|Click links|Direction to page|Navigation is successful|
<details><summary>Images</summary>
![](https://)

</details>
</details>



Site Owner
8. As the site owner, I would like...

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Responsivness|Site viewport is resized|Good view on mobile|Site is responsive|
|Validation|Form data entered|Errors are displayed where applicable| Success |

<details><summary>Images</summary>

</details>

### Automated Testing

 <details><summary>View automated testing</summary>

- Automated testing was done using the unittest and coverage librararies for Python.


### Unit Tests
- Test...

<img src="">

- Test results....

<img src="">

### Coverage 

- Coverage was installed via the terminal, pip install coverage
<img src="">


- Coverage was then used to test using the following...
<img src="">


- The results of the test were the following:
<img src="">

- A HTML report was also generated using the command, coverage html
<img src="">

</details>






[Back to Top](<#table-of-content>)
## Bugs

| **Bug** | **Fix** |
| ----------- | ----------- |
| **Bug** | **Fix** |
| Bug I had | I fixed it by... |



[Back to Top](<#table-of-content>)
## Deployment
### Heroku / Firebase

[Official Page](https://devcenter.heroku.com/articles/git) (Ctrl + click)
1. Log in to your account at heroku.com.
2. Create a new app, add a unique app name and choose your region.
3. Click on create app.
4. Go to "Settings".
5. Under Config Vars store any sensitive data in .json file. Name 'Key' field, copy the .json file paste it to 'Value' field. Also add a key 'PORT' and value '8000'.
6. Add required buildpacks. For this project, I set up 'Python' and 'node.js' in that order.
7. Go to "Deploy" and select "GitHub" in "Deployment method"
8. To link up the Heroku app to our Github repository code enter your repository name, click 'Search' and then 'Connect' when it shows below.
9.  Choose the branch you want to buid your app from.
10. If prefered, click on "Enable Automatic Deploys", which keeps the app up to date with your GitHub repository
11. Wait for the app to build. Once ready you will see the “App was successfully deployed” message and a 'View' button to take you to your deployed link.

### Fork Repository
To fork the repository by following these steps:
1. Go to the GitHub repository
2. Click on Fork button in upper right hand corner

### Clone Repository
You can clone the repository by following these steps:
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it 
3. Select if you prefere to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7.Press Enter to create your local clone.

[Back to Top](<#table-of-content>)
## Credits


### Media
- [Favicon](https://favicon.io/): Witch Icon</a>
- [Card Images](https://www.pexels.com/)</a>

### Code
- [Site](https://www.google.com)


## Acknowledgements

### Special thanks to the following:
- Code Institute
- Mo Shami
- My friends, family and my wonderful wife.
- 

[Back to Top](<#table-of-content>)