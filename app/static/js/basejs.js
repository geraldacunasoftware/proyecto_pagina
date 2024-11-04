$(document).ready(function () {
    // Efecto de desvanecimiento para la imagen principal
    setTimeout(function() {
        $('.fade-in-image').addClass('visible'); // Hace visible la imagen principal suavemente
    }, 500); // Retraso de 500 ms antes de mostrar la imagen

    // Efecto de desvanecimiento para las secciones al hacer scroll
    const sections = $('.fade-in-section');

    $(window).on('scroll', function () {
        const scrollTop = $(this).scrollTop();
        const windowHeight = $(this).height();

        sections.each(function () {
            const sectionTop = $(this).offset().top;

            if (scrollTop + windowHeight > sectionTop + 100) {
                $(this).addClass('visible'); // Agrega la clase para mostrar el efecto
            }
        });
    });
});
