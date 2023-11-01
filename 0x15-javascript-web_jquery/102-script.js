$(document).ready(() => {
    $('#btn_translate').click(() => {
      $.post('https://www.fourtonfish.com/hellosalut/hello/', { lang: $('#language_code').val() }, (data, textStatus) => {
        $('#hello').text(data.hello);
      });
    });
  });
  