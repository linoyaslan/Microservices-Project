var canvas = document.getElementById('ourCanvas');
var ctx = canvas.getContext('2d');

function color(color) {
	var select = document.getElementById('shapes');
	var shapes = select.options[select.selectedIndex].value;
	color_request(shapes, color);
}

function color_request(shapes, color) {
	clear(canvas, ctx);
	var img = new Image();
	img.onload = function() {
		ctx.drawImage(img, 250, 60);
	};
	//if (shapes == 'circle') port = 9999;
	if (shapes == 'circle') {
		console.log(circle_port);
		port = circle_port;
	}
	else if (shapes == 'square') {
		port = square_port;
	}
	else if (shapes == 'triangle') port = 9995;
	else if (shapes == 'rectangle') port = 9993;
	else if (shapes == 'rhombus') port = 9991;
	else if (shapes == 'pentagon') port = 9989;
	else if (shapes == 'hexagon') port = 9987;
	else if (shapes == 'oval') port = 9985;
	img.src = 'http://localhost:' + port + '/' + shapes + '/' + color;

	//window.onload = drawImage(canvas, ctx);
}
