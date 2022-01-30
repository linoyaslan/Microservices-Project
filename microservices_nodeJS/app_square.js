const express = require('express');
const app = express();
var path = require('path');
const RED = 'red';
const BLUE = 'blue';
const YELLOW = 'yellow';
const GREEN = 'green';

app.get('/', (req, res) => {
	res.send('MEOW!');
});

app.get('/square/:color', (req, res) => {
	var color = req.params.color;
	if (color == 'NONE') res.sendFile(path.resolve('square/square.png'));
	else if (color == 'RED') res.sendFile(path.resolve('square/square_red.png'));
	else if (color == 'YELLOW') res.sendFile(path.resolve('square/square_yellow.png'));
	else if (color == 'GREEN') res.sendFile(path.resolve('square/square_green.png'));
	else if (color == 'BLUE') res.sendFile(path.resolve('square/square_blue.png'));
});

app.listen(3000, () => {
	console.log('Listening on port 3000...');
});
