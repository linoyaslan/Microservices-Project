# Microservices Project

## Introduction:
An application that aims to provide services of drawing shapes on canvas with an option to paint according to the color chosen. There are 8 microservices in Flask, each with its own port, each service is basically an HTTP server that responds to get requests and so on, and there are 2 more microservices in nodeJS as well as HTTP servers that respond to requests and these are alternative microservices to the two of the microservices written in Flask.

## Technologies and Libraries
### our main app is created with:
* html, css and JS
* Bootstrap version: 4
### our microservices
* 8 of them in Flask
* 2 of them (back-up to app_circle.py and app_square.py) in nodeJS

## Setup:
### * To run the main app install it locally.
### * To run the microservices in Flask, make sure you intsall Flask before running. open 8 terminals, and run each command in different terminal:

```
$ python app_circle.py
$ python app_square.py
$ python app_triangle.py
$ python app_rectangle.py
$ python app_rhombus.py
$ python app_pentagon.py
$ python app_hexagon.py
$ python app_oval.py
```
each navigate to different port.

### * To run the microservices in nodeJS, make sure you have nodeJS installed in your computer. open 2 terminals, and run each command in different terminal:
```
$ npm i express
$ node app_circle.js
$ node app_square.js

```
## Running unit tests and Integration tests

### for tests in Flask run this:
```
$ python test.py

```
### for tests in nodeJS run this:
```
$ npm install supertest --save-dev
$ npm install --global mocha
$ mocha test.js

```
