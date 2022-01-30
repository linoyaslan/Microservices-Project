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

app.get('/circle/:color', (req, res) => {
	var color = req.params.color;
	if (color == 'NONE') res.sendFile(path.resolve('circle/circle.png'));
	else if (color == 'RED') res.sendFile(path.resolve('circle/circle_red.png'));
	else if (color == 'YELLOW') res.sendFile(path.resolve('circle/circle_yellow.png'));
	else if (color == 'GREEN') res.sendFile(path.resolve('circle/circle_green.png'));
	else if (color == 'BLUE') res.sendFile(path.resolve('circle/circle_blue.png'));
});

app.listen(3001, () => {
	console.log('Listening on port 3001...');
});
