function getClockElement(){
	return document.getElementById("clock");
}

function getCurrentTime(){
	const today = new Date();
	return `${today.getHours()}:${String(today.getMinutes()).padStart(2, "0")}:${String(today.getSeconds()).padStart(2, "0")}`;
}

function setClockUpdateInterval(clockElement){
	setInterval(function(){clockElement.innerHTML = getCurrentTime();}, 1000);
}

window.addEventListener("DOMContentLoaded", function(){
	const clockElement = getClockElement();
	setClockUpdateInterval(clockElement);
});