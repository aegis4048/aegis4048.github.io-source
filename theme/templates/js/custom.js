var COLLAPSE_WIDTH = 575;

function init_navbar () {
    $('.nav-link').on( {
        mouseenter: function () {
            $(this).addClass('hover');
        },
        mouseleave: function () {
            $(this).removeClass('hover');
        }
    });

    window.isCollapsed = true;
    $('.btn-search').on('click', function () {
        if (window.windowSize > COLLAPSE_WIDTH) {
            //$('#tipue_search_input').toggleClass('hidden');
            $('.navbar-nav').toggleClass('hidden');
        }
        window.isCollapsed = !isCollapsed
    });
}
function check_width() {
    window.windowSize = $(window).outerWidth();
    if (windowSize < COLLAPSE_WIDTH) {
        //$('#tipue_search_input').removeClass('hidden');
        $('.navbar-nav').removeClass('hidden');
        $('.nav-link').addClass('collapsed');
        $('#search-form').addClass('collapsed');
        $('#search-form.row').addClass('collapsed');
        $('.navbar-title').addClass('collapsed');
        $('.search-box-div').css('display', '');
        $('.search-box-div').addClass('row');

    }
    if (windowSize > COLLAPSE_WIDTH) {
        //$('#tipue_search_input').addClass('hidden');
        //$('#search-btn').removeClass('hidden');
        $('.navbar-nav').removeClass('hidden');
        $('.nav-link').removeClass('collapsed');
        $('#search-form').removeClass('collapsed');
        $('#search-form.row').removeClass('collapsed');
        $('.navbar-brand').css('margin-left', '0');
        $('.navbar-toggler').css('margin-right', '0');
        $('.navbar-title').removeClass('collapsed');
        $('.search-box-div').css('display', 'inherit');
        $('.search-box-div').removeClass('row');
    }
}
function jupyter_css() {
    if (window.windowSize > 486) {
        $('.prompt').css('width', '69.53px');
    }
    $('.rendered_html th').css('background', 'unset')
}
$(document).ready(function() {
    check_width();
    $(window).resize(check_width);
    init_navbar();
    jupyter_css();
});