$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    $.get(
      'https://www.fourtonfish.com/hellosalut/',
      { lang: $('INPUT#language_code').val() },
      function (data) {
        $('DIV#hello').text(data.hello);
      }
    );
  });
});
