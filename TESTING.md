# **Litter Pickers London Testing Documentation**

## **Table of contents**
 - [**HTML Validation**](#html-validation)
 - [**CSS Validation**](#css-validation)
 - [**Python Validation**](#python-validation)
 - [**Lighthouse**](#lighthouse)
 - [**Bugs and Issues**](#bugs-and-issues)

<hr>

## **HTML Validation**

All HTML code has been run through the [W3C - HTML](https://validator.w3.org/) validator and returns no errors, results can be viewed below:

#### **Index.html**
![HTML Home Page](docs/testing/index.jpg)

#### **Events.html**
![HTML Events Page](docs/testing/events.jpg)

#### **Event-details.html**
![HTML Event-Details Page](docs/testing/event-detail.jpg)

#### **Add-event.html**
![HTML Add Event Page](docs/testing/add-event.jpg)

#### **Edit-event.html**
![HTML Edit Event Page](docs/testing/edit.jpg)

#### **Delete-event.html**
![HTML Delete Event Page](docs/testing/delete.jpg)

<hr>

## **CSS Validation**

All CSS code has been run through the [W3C - CSS](https://jigsaw.w3.org/css-validator/) validator and returns no errors, results can be viewed below:

![CSS Validator](docs/testing/css.jpg)


<hr>

## **Python Validation**

All Python code has been run through the [CI PEP8 Testing](https://pep8ci.herokuapp.com/) validator and has returned no errors, results can be viewed below:

#### **admin.py**
![admin-py](docs/testing/admin.jpg)

#### **app.py**
![app-py](docs/)



#### **forms.py**
![forms-py](docs/testing/forms.jpg)

#### **models.py**
![models-py](docs/testing/models.jpg)

#### **urls.py**
![urls-py](docs/testing/urls.jpg)

#### **views.py**
![views-py](docs/testing/views.jpg)

<hr>

## **Lighthouse**
- The lighthouse score results can be found below.

![Lighthouse](docs/testing/lighthouse.jpg)

## **Bugs and Issues**
- I was hoping that unapproved comments would display to the user but have been unable to get this to work in the time available.
- I had originally set up the urls so that the url was unique, but realised duplicate event names would result in duplicate slugs, so included the event id within the slug.