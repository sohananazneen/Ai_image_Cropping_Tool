document.addEventListener("DOMContentLoaded", function () {
  const canvas = document.getElementById("imageCanvas");
  const ctx = canvas.getContext("2d");
  let img = new Image();
  img.src = "/static/cropped_image.jpg"; // Replace with the correct route to the cropped image

  img.onload = function () {
    canvas.width = img.width;
    canvas.height = img.height;
    ctx.drawImage(img, 0, 0, img.width, img.height);
  };
});
