// JavaScript para manejar la selección exclusiva de las casillas
document.addEventListener('DOMContentLoaded', function() {
    var checkboxes = document.querySelectorAll('input[name="checkboxGroup"]');
    checkboxes.forEach(function(checkbox) {
      checkbox.addEventListener('change', function() {
        checkboxes.forEach(function(otherCheckbox) {
          if (otherCheckbox !== checkbox) otherCheckbox.checked = false;
        });
      });
    });
  });
  
