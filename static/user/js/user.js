// event.PreventDefault()
// event.stopPropagation()

function login (url) {
  $('#login').load(url, function() {
    $(this).modal('show');
  });
  event.stopPropagation()
}

function signin (url) {
  $('#signin').load(url, function() {
    $(this).modal('show');
  });
  event.stopPropagation()
}