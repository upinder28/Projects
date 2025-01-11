// Background js
document.addEventListener("DOMContentLoaded", function () {
    const colorPicker = document.getElementById("color-picker");
    const colors = document.querySelectorAll(".color");

    colorPicker.addEventListener("input", function () {
        const selectedColor = colorPicker.value;
        document.body.style.backgroundColor = selectedColor;
    });

    colors.forEach(color => {
        color.addEventListener("click", function () {
            const selectedColor = window.getComputedStyle(color).getPropertyValue("--color");
            document.body.style.backgroundColor = selectedColor;
            colorPicker.value = selectedColor;
        });
    });
// Container js
    const colorPicker2 = document.getElementById("color-picker2");
    const container = document.querySelector(".container");

    colorPicker2.addEventListener("input", function () {
        const color = colorPicker2.value;
        container.style.backgroundColor = color; 
    });
});