var canvas = document.getElementById('ourCanvas');
var ctx = canvas.getContext('2d');
var circle_port;
var square_port;
async function draw(option) {
	shape_request(option);
	switch (option) {
		case 'circle':
			var bool = await check_liveness(option, 9999);
			console.log('check_liveness Val :' + bool);
			if (bool === 1) {
				shape_request(option, 9999);
				console.log('success 9999');
				circle_port = 9999;
			}
			else {
				alert('There is a problem with the connection to the server. check for another one ...');
				shape_request(option, 3001);
				console.log('success 3001');
				circle_port = 3001;
			}
			break;
		case 'square':
			var bool = await check_liveness(option, 9997);
			console.log('check_liveness Val :' + bool);
			if (bool === 1) {
				shape_request(option, 9997);
				console.log('success 9997');
				square_port = 9997;
			}
			else {
				alert('There is a problem with the connection to the server. check for another one ...');
				shape_request(option, 3000);
				console.log('success 3000');
				square_port = 3000;
			}
			break;
		case 'triangle':
			shape_request(option, 9995);
			break;
		case 'rectangle':
			shape_request(option, 9993);
			break;
		case 'rhombus':
			shape_request(option, 9991);
			break;
		case 'pentagon':
			shape_request(option, 9989);
			break;
		case 'hexagon':
			shape_request(option, 9987);
			break;
		case 'oval':
			shape_request(option, 9985);
			break;
	}
	// reset the select colors
	document.getElementById('colors').selectedIndex = 0;
}

function shape_request(option, port) {
	clear(canvas, ctx);
	var img = new Image();
	img.onload = function() {
		ctx.drawImage(img, 250, 60);
	};
	img.src = 'http://localhost:' + port + '/' + option + '/NONE';
}

async function check_liveness(option, port) {
	var url = 'http://localhost:' + port + '/' + option + '/NONE';
	var status;
	try {
		const response = await fetch(url);
		console.log(response);
		status = response.status;
	} catch (e) {
		console.log(e);
		return 0;
	}
	if (status === 200) {
		return 1;
	}
	else {
		return 0;
	}
}
