// event.PreventDefault()
// event.stopPropagation()

$('#table_hardware_control').on('click', '.clickable-row', function(event) {
  $(this).addClass('active').siblings().removeClass('active');
  $('#update').removeClass('disabled');
  $('#delete').removeClass('disabled');
  $('#action').removeClass('disabled');
});
