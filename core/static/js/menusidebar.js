document.addEventListener('DOMContentLoaded', function() {
    var menuTrigger = document.getElementById('js-menu-trigger');
    var sideMenu = document.getElementById('js-menu');
    var body = document.body;

    // Función para alternar la clase 'active' que controla la visibilidad del menú
    function toggleMenu() {
        sideMenu.classList.toggle('active');
        body.classList.toggle('menu-active');
    }

    // Evento para escuchar el clic en el botón del menú
    menuTrigger.addEventListener('click', function(e) {
        e.preventDefault();
        toggleMenu();
    });

    // Opcional: Cerrar el menú si se hace clic fuera de él
    document.addEventListener('click', function(e) {
        if (!sideMenu.contains(e.target) && !menuTrigger.contains(e.target)) {
            if (sideMenu.classList.contains('active')) {
                toggleMenu();
            }
        }
    });
});
