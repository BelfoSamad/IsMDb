$(document).ready(function () {

    // $('#sidebarCollapse').on('click', function () {
    //     $('#sidebar').toggleClass('active');
    //     $(this).toggleClass('active');
    // });

    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.datepicker').datepicker({
        format : 'yyyy-mm-dd'
        }
    );
    $('.timepicker').timepicker();
  $('.dropdown-trigger').dropdown({
   belowOrigin: true
});
    $('.modal').modal({
        dismissible : false
    });
});