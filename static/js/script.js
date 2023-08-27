// Closes messages after 2.5 secs
$(document).ready(function () {
    setTimeout(function () {
        let messages = document.getElementById("msg");
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 2500);
});