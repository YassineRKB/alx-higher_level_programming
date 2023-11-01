$(document).ready(() => {
    $('#language_code').keypress(event => {
      if (event.which === 13) {
        $('#btn_translate').click();
      }
    });
    $('#btn_translate').click(() => {
      $.post('https://www.fourtonfish.com/hellosalut/hello/', { lang: $('#language_code').val() }, (data, textStatus) => {
        $('#hello').text(data.hello);
      });
    });
  });
  