document.addEventListener("DOMContentLoaded", function () {
  const deleteField = document.getElementById("delete_image");
  if (!deleteField) return;

  const group = deleteField.closest(".form-group");
  if (group) group.style.display = "none";

  const button = document.createElement("button");
  button.type = "button";
  button.className = "btn btn-outline-danger mb-3";
  button.innerHTML = '<i class="fa-solid fa-trash"></i> Delete image';
  button.addEventListener("click", function () {
    if (!window.confirm("Delete the current image? Save the form to apply this change.")) return;
    deleteField.value = "1";
    button.disabled = true;
    button.innerHTML = "Image will be deleted when you save";
  });
  (group || deleteField).after(button);
});
