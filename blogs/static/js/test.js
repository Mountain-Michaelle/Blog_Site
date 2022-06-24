var today = new Date();
var hourNow = today.getHours();
var greetings;

if (hourNow < 12) {
    greetings = "Good Morning Dear!";

    if (hourNow > 12) {
        greetings = " Good Afternoon ";
    }
    if (hourNow > 16) {
        greetings = " Good Evening";
    }
}

var elgreeting = document.getElementById('greeting');
elgreeting.textContent = greetings