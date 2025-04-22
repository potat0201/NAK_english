document
  .getElementById("chatbot-toggle")
  .addEventListener("click", function () {
    const container = document.getElementById("chatbot-container");
    if (container.style.display === "none") {
      container.style.display = "block";
      // Load nội dung chat khi mở
      fetch("/chatbot/")
        .then((response) => response.text())
        .then((html) => {
          container.innerHTML = html;
        });
    } else {
      container.style.display = "none";
    }
  });
