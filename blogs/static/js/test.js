var today = new Date();
var hourNow = today.getHours();
var greetings;

if (hourNow < 12) {
    greetings = "Good morning";
    if (hourNow != 12 && 13 && 14 && 15) {
        greetings = "Good Evenin";
    }
} else {
    greetings = " Good Afternoon";
}


var elgreeting = document.getElementById('greeting');
elgreeting.textContent = greetings;