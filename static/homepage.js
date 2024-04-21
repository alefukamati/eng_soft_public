document.getElementById("irLogin").addEventListener("click", function () {
    window.location.href = "/login";
  });
  document.getElementById("irInfoAVC").addEventListener("click", function () {
    const targetElement = document.getElementById("sobre");
    const targetPosition = targetElement.offsetTop;
    window.scrollTo({
      top: targetPosition,
      behavior: "smooth",
    });
  });
  document
    .getElementById("irInfoIniciativa")
    .addEventListener("click", function () {
      const targetElement = document.getElementById("iniciativa");
      const targetPosition = targetElement.offsetTop;
      window.scrollTo({
        top: targetPosition,
        behavior: "smooth",
      });
    });