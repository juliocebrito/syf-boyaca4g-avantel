$('#sidebar-toggle').on('click', function (event) {
  $('.sidebar').toggleClass('d-md-block');
  $('#dashboard').toggleClass('content_dashboard');
  $('#nav_dasboard').toggleClass('content_nav');
});

$('#filter-toggle').on('click', function (event) {
  $('.filter').toggleClass('d-md-block');
  $('#dashboard').toggleClass('content_dashboard_filter');
  $('#nav_dasboard').toggleClass('content_nav_filter');
});


function search_url (form) {
  var current_url = window.location.href;
  var url_search_hardware = '/hardware/hardware/search/';
  var url_search_hardware_control = '/hardware/hardware/control/search/';

  if (current_url.includes('/hardware/hardware/control/')) {
    form.action = url_search_hardware_control;
  } else if (current_url.includes('/hardware/hardware/')) {
    form.action = url_search_hardware;
  }
  else {
    form.action = ''
  }
}

function filter_url (form) {
  var current_url = window.location.href;
  var url_filter_hardware = '/hardware/hardware/filter/';
  var url_filter_hardware_control = '/hardware/hardware/control/filter/';

  if (current_url.includes('/hardware/hardware/control/')) {
    form.action = url_filter_hardware_control;
  } else if (current_url.includes('/hardware/hardware/')) {
    form.action = url_filter_hardware;
  }
  else {
    form.action = ''
  }
}

$("#paginate_by").on('change', function () {
  $(this).submit()
});