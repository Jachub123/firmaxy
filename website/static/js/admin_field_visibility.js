document.addEventListener("DOMContentLoaded", function () {
  const areaField = document.getElementById("id_area");
  const nameField = document.getElementById("id_name");
  const widthField = document.getElementById("id_width");
  const heightField = document.getElementById("id_height");

  function toggleFields() {
    if (areaField.value === "G") {
      nameField.parentElement.parentElement.classList.remove("hidden");
      widthField.parentElement.parentElement.parentElement.classList.remove("hidden");
      heightField.parentElement.parentElement.parentElement.classList.remove("hidden");
      if (document.getElementsByTagName("h2")[0] === undefined) {
        nameField.value = "";
      } else {
        nameField.value = document.getElementsByTagName("h2")[0].innerHTML;
      }
    } else {
      if (areaField.value === "HP") {
        nameField.value = "StartBild";
      } else if (areaField.value === "AM") {
        nameField.value = "ÜbermichBild";
      } else if (areaField.value === "AMSL") {
        nameField.value = "ÜbermichBildkleinL";
      } else if (areaField.value === "AMSR") {
        nameField.value = "ÜbermichBildkleinR";
      }
      nameField.parentElement.parentElement.classList.add("hidden");
      heightField.parentElement.parentElement.parentElement.classList.add("hidden");
      widthField.parentElement.parentElement.parentElement.classList.add("hidden");
    }
  }

  toggleFields();

  areaField.addEventListener("change", (e) => {
    toggleFields();
  });
});
