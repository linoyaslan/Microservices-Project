import os
import subprocess
import time
import unittest
import urllib.request as urllib2

import pytest

import app_circle, app_triangle, app_hexagon, app_oval, app_pentagon, app_rectangle, app_rhombus, app_square
from flask_testing import LiveServerTestCase
from flask import Flask
from nose.tools import assert_true
import requests
import threading


class Test(unittest.TestCase):
    def setUp(self):
        self.app_triangle = app_triangle.app.test_client()
        self.app_circle = app_circle.app.test_client()
        self.app_hexagon = app_hexagon.app.test_client()
        self.app_oval = app_oval.app.test_client()
        self.app_pentagon = app_pentagon.app.test_client()
        self.app_rectangle = app_rectangle.app.test_client()
        self.app_rhombus = app_rhombus.app.test_client()
        self.app_square = app_square.app.test_client()

    def tearDown(self):
        pass

    ## unitests app_triangle ##
    def test_draw_triangle(self):
        response1 = self.app_triangle.get('/triangle/NONE', follow_redirects=True)
        response2 = self.app_triangle.get('/triangl/NONE', follow_redirects=True)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 404)

    def test_draw_triangle_red(self):
        response = self.app_triangle.get('/triangle/RED', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_draw_triangle_blue(self):
        response = self.app_triangle.get('/triangle/BLUE', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_draw_triangle_green(self):
        response = self.app_triangle.get('/triangle/GREEN', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_draw_triangle_yellow(self):
        response = self.app_triangle.get('/triangle/YELLOW', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    ## unitests app_triangle ##

    ## unitests app_circle ##
    def test_draw_circle(self):
        response1 = self.app_circle.get('/circle/NONE', follow_redirects=True)
        response2 = self.app_circle.get('/circl/NONE', follow_redirects=True)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 404)

    def test_draw_circle_red(self):
        response = self.app_circle.get('/circle/RED', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_draw_circle_blue(self):
        response = self.app_circle.get('/circle/BLUE', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_draw_circle_green(self):
        response = self.app_circle.get('/circle/GREEN', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_draw_circle_yellow(self):
        response = self.app_circle.get('/circle/YELLOW', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    ## unitests app_circle ##

    ## unitests app_hexagon ##
    def test_draw_hexagon(self):
        response1 = self.app_hexagon.get('/hexagon/NONE', follow_redirects=True)
        response2 = self.app_hexagon.get('/hexago/NONE', follow_redirects=True)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 404)

    def test_draw_hexagon_red(self):
        response = self.app_hexagon.get('/hexagon/RED', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_draw_hexagon_blue(self):
        response = self.app_hexagon.get('/hexagon/BLUE', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_draw_hexagon_green(self):
        response = self.app_hexagon.get('/hexagon/GREEN', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_draw_hexagon_yellow(self):
        response = self.app_hexagon.get('/hexagon/YELLOW', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    ## unitests app_hexagon ##

    ## unitests app_oval ##
    def test_draw_oval(self):
        response1 = self.app_oval.get('/oval/NONE', follow_redirects=True)
        response2 = self.app_oval.get('/ova/NONE', follow_redirects=True)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 404)

    def test_draw_oval_red(self):
        response = self.app_oval.get('/oval/RED', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_draw_oval_blue(self):
        response = self.app_oval.get('/oval/BLUE', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_draw_oval_green(self):
        response = self.app_oval.get('/oval/GREEN', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_draw_oval_yellow(self):
        response = self.app_oval.get('/oval/YELLOW', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    ## unitests app_oval ##

    ## unitests app_pentagon ##
    def test_draw_pentagon(self):
        response1 = self.app_pentagon.get('/pentagon/NONE', follow_redirects=True)
        response2 = self.app_pentagon.get('/pentago/NONE', follow_redirects=True)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 404)

    def test_draw_pentagon_red(self):
        response = self.app_pentagon.get('/pentagon/RED', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_draw_pentagon_blue(self):
        response = self.app_pentagon.get('/pentagon/BLUE', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_draw_pentagon_green(self):
        response = self.app_pentagon.get('/pentagon/GREEN', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_draw_pentagon_yellow(self):
        response = self.app_pentagon.get('/pentagon/YELLOW', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    ## unitests app_pentagon ##

    ## unitests app_rectangle ##
    def test_draw_rectangle(self):
        response1 = self.app_rectangle.get('/rectangle/NONE', follow_redirects=True)
        response2 = self.app_rectangle.get('/rectangl/NONE', follow_redirects=True)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 404)

    def test_draw_rectangle_red(self):
        response = self.app_rectangle.get('/rectangle/RED', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_draw_rectangle_blue(self):
        response = self.app_rectangle.get('/rectangle/BLUE', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_draw_rectangle_green(self):
        response = self.app_rectangle.get('/rectangle/GREEN', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_draw_rectangle_yellow(self):
        response = self.app_rectangle.get('/rectangle/YELLOW', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    ## unitests app_rectangle ##

    ## unitests app_rhombus ##
    def test_draw_rhombus(self):
        response1 = self.app_rhombus.get('/rhombus/NONE', follow_redirects=True)
        response2 = self.app_rhombus.get('/rhombu/NONE', follow_redirects=True)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 404)

    def test_draw_rhombus_red(self):
        response = self.app_rhombus.get('/rhombus/RED', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_draw_rhombus_blue(self):
        response = self.app_rhombus.get('/rhombus/BLUE', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_draw_rhombus_green(self):
        response = self.app_rhombus.get('/rhombus/GREEN', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_draw_rhombus_yellow(self):
        response = self.app_rhombus.get('/rhombus/YELLOW', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    ## unitests app_rhombus ##

    ## unitests app_square ##
    def test_draw_square(self):
        response1 = self.app_square.get('/square/NONE', follow_redirects=True)
        response2 = self.app_square.get('/squar/NONE', follow_redirects=True)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 404)

    def test_draw_square_red(self):
        response = self.app_square.get('/square/RED', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_draw_square_blue(self):
        response = self.app_square.get('/square/BLUE', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_draw_square_green(self):
        response = self.app_square.get('/square/GREEN', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_draw_square_yellow(self):
        response = self.app_square.get('/square/YELLOW', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    ## unitests app_square ##

    ## Integration test app_circle ##
    def test_draw_circle_integration_test(self):
        proc = subprocess.Popen(["python","app_circle.py"])
        none_request = requests.get('http://localhost:9999/circle/NONE')
        red_request = requests.get('http://localhost:9999/circle/RED')
        blue_request = requests.get('http://localhost:9999/circle/BLUE')
        green_request = requests.get('http://localhost:9999/circle/GREEN')
        yellow_request = requests.get('http://localhost:9999/circle/YELLOW')
        proc.terminate()
        self.assertEqual(none_request.status_code, 200)
        self.assertEqual(red_request.status_code, 200)
        self.assertEqual(blue_request.status_code, 200)
        self.assertEqual(green_request.status_code, 200)
        self.assertEqual(yellow_request.status_code, 200)

    ## Integration test app_triangle ##
    def test_draw_triangle_integration_test(self):
        proc = subprocess.Popen(["python","app_triangle.py"])
        none_request = requests.get('http://localhost:9995/triangle/NONE')
        red_request = requests.get('http://localhost:9995/triangle/RED')
        blue_request = requests.get('http://localhost:9995/triangle/BLUE')
        green_request = requests.get('http://localhost:9995/triangle/GREEN')
        yellow_request = requests.get('http://localhost:9995/triangle/YELLOW')
        proc.terminate()
        self.assertEqual(none_request.status_code, 200)
        self.assertEqual(red_request.status_code, 200)
        self.assertEqual(blue_request.status_code, 200)
        self.assertEqual(green_request.status_code, 200)
        self.assertEqual(yellow_request.status_code, 200)

    ## Integration test app_square ##
    def test_draw_square_integration_test(self):
        proc = subprocess.Popen(["python","app_square.py"])
        none_request = requests.get('http://localhost:9997/square/NONE')
        red_request = requests.get('http://localhost:9997/square/RED')
        blue_request = requests.get('http://localhost:9997/square/BLUE')
        green_request = requests.get('http://localhost:9997/square/GREEN')
        yellow_request = requests.get('http://localhost:9997/square/YELLOW')
        proc.terminate()
        self.assertEqual(none_request.status_code, 200)
        self.assertEqual(red_request.status_code, 200)
        self.assertEqual(blue_request.status_code, 200)
        self.assertEqual(green_request.status_code, 200)
        self.assertEqual(yellow_request.status_code, 200)

    ## Integration test app_rhombus ##
    def test_draw_rhombus_integration_test(self):
        proc = subprocess.Popen(["python","app_rhombus.py"])
        none_request = requests.get('http://localhost:9991/rhombus/NONE')
        red_request = requests.get('http://localhost:9991/rhombus/RED')
        blue_request = requests.get('http://localhost:9991/rhombus/BLUE')
        green_request = requests.get('http://localhost:9991/rhombus/GREEN')
        yellow_request = requests.get('http://localhost:9991/rhombus/YELLOW')
        proc.terminate()
        self.assertEqual(none_request.status_code, 200)
        self.assertEqual(red_request.status_code, 200)
        self.assertEqual(blue_request.status_code, 200)
        self.assertEqual(green_request.status_code, 200)
        self.assertEqual(yellow_request.status_code, 200)

    ## Integration test app_rectangle ##
    def test_draw_rectangle_integration_test(self):
        proc = subprocess.Popen(["python","app_rectangle.py"])
        none_request = requests.get('http://localhost:9993/rectangle/NONE')
        red_request = requests.get('http://localhost:9993/rectangle/RED')
        blue_request = requests.get('http://localhost:9993/rectangle/BLUE')
        green_request = requests.get('http://localhost:9993/rectangle/GREEN')
        yellow_request = requests.get('http://localhost:9993/rectangle/YELLOW')
        proc.terminate()
        self.assertEqual(none_request.status_code, 200)
        self.assertEqual(red_request.status_code, 200)
        self.assertEqual(blue_request.status_code, 200)
        self.assertEqual(green_request.status_code, 200)
        self.assertEqual(yellow_request.status_code, 200)

    ## Integration test app_pentagon ##
    def test_draw_pentagon_integration_test(self):
        proc = subprocess.Popen(["python","app_pentagon.py"])
        none_request = requests.get('http://localhost:9989/pentagon/NONE')
        red_request = requests.get('http://localhost:9989/pentagon/RED')
        blue_request = requests.get('http://localhost:9989/pentagon/BLUE')
        green_request = requests.get('http://localhost:9989/pentagon/GREEN')
        yellow_request = requests.get('http://localhost:9989/pentagon/YELLOW')
        proc.terminate()
        self.assertEqual(none_request.status_code, 200)
        self.assertEqual(red_request.status_code, 200)
        self.assertEqual(blue_request.status_code, 200)
        self.assertEqual(green_request.status_code, 200)
        self.assertEqual(yellow_request.status_code, 200)

    ## Integration test app_oval ##
    def test_draw_oval_integration_test(self):
        proc = subprocess.Popen(["python","app_oval.py"])
        none_request = requests.get('http://localhost:9985/oval/NONE')
        red_request = requests.get('http://localhost:9985/oval/RED')
        blue_request = requests.get('http://localhost:9985/oval/BLUE')
        green_request = requests.get('http://localhost:9985/oval/GREEN')
        yellow_request = requests.get('http://localhost:9985/oval/YELLOW')
        proc.terminate()
        self.assertEqual(none_request.status_code, 200)
        self.assertEqual(red_request.status_code, 200)
        self.assertEqual(blue_request.status_code, 200)
        self.assertEqual(green_request.status_code, 200)
        self.assertEqual(yellow_request.status_code, 200)

    ## Integration test app_oval ##
    def test_draw_hexagon_integration_test(self):
        proc = subprocess.Popen(["python","app_hexagon.py"])
        none_request = requests.get('http://localhost:9987/hexagon/NONE')
        red_request = requests.get('http://localhost:9987/hexagon/RED')
        blue_request = requests.get('http://localhost:9987/hexagon/BLUE')
        green_request = requests.get('http://localhost:9987/hexagon/GREEN')
        yellow_request = requests.get('http://localhost:9987/hexagon/YELLOW')
        proc.terminate()
        self.assertEqual(none_request.status_code, 200)
        self.assertEqual(red_request.status_code, 200)
        self.assertEqual(blue_request.status_code, 200)
        self.assertEqual(green_request.status_code, 200)
        self.assertEqual(yellow_request.status_code, 200)
if __name__ == '__main__':
    unittest.main()
