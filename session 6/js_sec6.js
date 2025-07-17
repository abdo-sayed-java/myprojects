document.getElementById("info").addEventListener("submit", function (e) {
  e.preventDefault();

  const nameInput = document.getElementById("name");
  const emailInput = document.getElementById("email");
  const bioInput = document.getElementById("bio");

  const nameError = document.getElementById("name-error");
  const emailError = document.getElementById("email-error");
  const bioError = document.getElementById("bio-error");

  const displayInfo = document.getElementById("display-info");

  nameError.textContent = "";
  emailError.textContent = "";
  bioError.textContent = "";

  if (nameInput.value.trim() === "") {
    nameError.textContent = "Name is required.";
    return;
  }
  if (emailInput.value.trim() === "") {
    emailError.textContent = "Email is required.";
    return;
  }
  if (!emailInput.value.includes("@")) {
    emailError.textContent = "Email must contain '@'.";
    return;
  }
  if (bioInput.value.trim() === "") {
    bioError.textContent = "bio is required.";
    return;
  }

  displayInfo.innerHTML = `
        <h3>Your Profile</h3>
        <p><strong>Name:</strong> ${nameInput.value}</p>
        <p><strong>Email:</strong> ${emailInput.value}</p>
        <p><strong>Bio:</strong> ${bioInput.value}</p>
      `;
});
