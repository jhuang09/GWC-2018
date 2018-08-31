function navBar(){
	document.getElementById("navMenu").innerHTML =
 	"<div class=\"banner\">" +
		"<nav style=\"width: max-content;\">" +
		"<a href=\"home.html\">Home</a>"+
			"<div class=\"drop\">" +
				"<button class=\"dropbtn\">Menu</button>" +
				"<div class=\"dropdown\">" +
					"<a href=\"prof.html\">About Me</a>" +
					"<a href=\"portfolio.html\">Portfolio</a>" +
					"<a href=\"contact.html\">Contact</a>" +
					"<a href=\"js_fun.html\">Fun with JS</a>" +
				"</div>" +
			"</div>" +
		"</nav>" +
	"</div>";

}

function displayClock(){
	var clock = document.getElementById('clock');
	var now = new Date();
	var hours = now.getHours();
	var minutes = now.getMinutes();
	var seconds = now.getSeconds();

	if (minutes < 10){
		minutes = "0" + minutes;
	}
	if(seconds < 10){
		seconds = "0" + seconds;
	}
	if(hours > 12 && hours < 24){
		var timeOfDay = "pm";
		hours -= 12;
	}
	else{
		var timeOfDay = "am";
	}

	var currentTime = hours + ":" + minutes + ":" + seconds + timeOfDay;

	clock.innerHTML = currentTime;
}

function toggleClock(){
	var clock = document.getElementById("clock");
	var display = clock.style.display;
	var clockbtn = document.getElementById("clockbtn");

	if (display == "block"){
		clock.style.display = "none";
		clockbtn.innerHTML = "Show clock";
	}
	else{
		clock.style.display = "block";
		clockbtn.innerHTML = "Hide clock";
	}
}

/*function enlargeText(){
	var paragraph = document.getElementsByTagName('p');
	paragraph[1].style.fontSize="36px";
}*/

/* creates canvas for interactive! */
/* creates drawing object for canvas */
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
ctx.fillStyle = "white";
ctx.fillRect(0,0,canvas.width,canvas.height);
canvas.addEventListener("click", function clear(){
	ctx.fillStyle = "white";
	ctx.fillRect(0,0,canvas.width,canvas.height);
});
canvas.addEventListener("mousemove", function myFunction(){
	canvas.onmousemove = function(e){
	var r = Math.floor(Math.random() * 255 + 1),
	    g = Math.floor(Math.random() * 255 + 1),
	    b = Math.floor(Math.random() * 255 + 1);
	var color = "rgb(" + r + "," + g + "," + b + ")";
	ctx.fillStyle = color;
	var rect = canvas.getBoundingClientRect();
	var x = e.clientX - rect.left;
	var y = e.clientY - rect.top;
	ctx.beginPath();
	ctx.arc(x, y, Math.floor(Math.random() * 30 + 1), 0, 2 * Math.PI);
	//ctx.stroke();
	ctx.fill();
	}

});

// $(".parent").on("click", function(){
// 	$(this).toggleClass("trash"); //click will transform or bring it back
// });
