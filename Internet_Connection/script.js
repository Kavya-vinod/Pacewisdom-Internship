let message = document.getElementById("message");

let messageOnline = () => {
  message.textContent = "Internet Connection Available";
  message.style.backgroundColor = "rgba(0, 0, 0, 0.6)"; // Semi-transparent black background
  message.style.color = "#fff"; // White text color
};
let messageOffline = () => {
  message.textContent = "No Internet Connection";
  message.style.backgroundColor = "rgba(0, 0, 0, 0.6)"; // Semi-transparent black background
  message.style.color = "#fff"; // White text color
};

if (window.navigator.onLine) {
  messageOnline();
} else {
  messageOffline();
}

window.addEventListener("online", messageOnline);
window.addEventListener("offline", messageOffline);
