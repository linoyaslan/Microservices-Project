const assert = require('assert');
const request = require('supertest');
var express = require('express');
const { spawn } = require('child_process');

var app_circle = express();
var app_square = express();

app_circle.set('port', 3001);
app_square.set('port', 3000);

// Unit tests app_circle //
describe('Unit testing the /circle/NONE route', function() {
	it('should return OK status', function() {
		request(app_circle).get('/circle/NONE').then(function(response) {
			assert.equal(response.status, 200);
		});
	});

	it('should return OK status', function() {
		request(app_circle).get('/circl/NONE').then(function(response) {
			assert.equal(response.status, 404);
		});
	});
});

describe('Unit testing the /circle/RED route', function() {
	it('should return OK status', function() {
		request(app_circle).get('/circle/RED').then(function(response) {
			assert.equal(response.status, 200);
		});
	});
});

describe('Unit testing the /circle/BLUE route', function() {
	it('should return OK status', function() {
		request(app_circle).get('/circle/BLUE').then(function(response) {
			assert.equal(response.status, 200);
		});
	});
});

describe('Unit testing the /circle/GREEN route', function() {
	it('should return OK status', function() {
		request(app_circle).get('/circle/GREEN').then(function(response) {
			assert.equal(response.status, 200);
		});
	});
});

describe('Unit testing the /circle/YELLOW route', function() {
	it('should return OK status', function() {
		request(app_circle).get('/circle/YELLOW').then(function(response) {
			assert.equal(response.status, 200);
		});
	});
});
// Unit tests app_circle //

// Unit tests app_square //
describe('Unit testing the /square/NONE route', function() {
	it('should return OK status', function() {
		request(app_square).get('/square/NONE').then(function(response) {
			assert.equal(response.status, 200);
		});
	});

	it('should return OK status', function() {
		request(app_square).get('/squar/NONE').then(function(response) {
			assert.equal(response.status, 404);
		});
	});
});

describe('Unit testing the /square/RED route', function() {
	it('should return OK status', function() {
		request(app_square).get('/square/RED').then(function(response) {
			assert.equal(response.status, 200);
		});
	});
});

describe('Unit testing the /square/BLUE route', function() {
	it('should return OK status', function() {
		request(app_square).get('/square/BLUE').then(function(response) {
			assert.equal(response.status, 200);
		});
	});
});

describe('Unit testing the /square/GREEN route', function() {
	it('should return OK status', function() {
		request(app_square).get('/square/GREEN').then(function(response) {
			assert.equal(response.status, 200);
		});
	});
});

describe('Unit testing the /square/YELLOW route', function() {
	it('should return OK status', function() {
		request(app_square).get('/square/YELLOW').then(function(response) {
			assert.equal(response.status, 200);
		});
	});
});

// Unit tests app_square //

// Intgeration Tests app_circle //
describe('Integration testing to the app_circle server ', function() {
	it('should return OK status', function() {
		var proc = require('child_process').exec('node app_circle.js');
		request(app_circle).get('/circle/NONE').then(function(response) {
			assert.equal(response.status, 200);
		});
		request(app_circle).get('/circle/RED').then(function(response) {
			assert.equal(response.status, 200);
		});
		request(app_circle).get('/circle/YELLOW').then(function(response) {
			assert.equal(response.status, 200);
		});
		request(app_circle).get('/circle/GREEN').then(function(response) {
			assert.equal(response.status, 200);
		});
		request(app_circle).get('/circle/BLUE').then(function(response) {
			assert.equal(response.status, 200);
		});
		proc.kill('SIGINT');
	});
});
// Intgeration Tests app_circle //

// Intgeration Tests app_square //
describe('Integration testing to the app_square server ', function() {
	it('should return OK status', function() {
		var proc = require('child_process').exec('node app_square.js');
		request(app_square).get('/square/NONE').then(function(response) {
			assert.equal(response.status, 200);
		});
		request(app_square).get('/square/RED').then(function(response) {
			assert.equal(response.status, 200);
		});
		request(app_square).get('/square/YELLOW').then(function(response) {
			assert.equal(response.status, 200);
		});
		request(app_square).get('/square/GREEN').then(function(response) {
			assert.equal(response.status, 200);
		});
		request(app_square).get('/square/BLUE').then(function(response) {
			assert.equal(response.status, 200);
		});
		proc.kill('SIGINT');
	});
});
// Intgeration Tests app_square //
