(function() {

  /* Initialize filter inputs */
  var defaultText = $('.textFilter-input').val();

  $('.textFilter-input')
    .focus(function(e) {
      if ($(this).val() === defaultText)
        $(this).val('');
    })
    .blur(function(e) {
      if ($(this).val() === '')
        $(this).val(defaultText);
    })
    .keyup(function(e) {
      var patterns = $(this).val().toLowerCase().split(' ');
      if (!patterns.length)
        return;
      $('.textFilter-target')
        .hide()
        .filter(function() {
          var matchText = $(this)
            .find('.textFilter-match')
            .text()
            .toLowerCase();
          for (var i = 0; i < patterns.length; i++)
            if (matchText.indexOf(patterns[i]) === -1)
              return false;
          return true;
        })
        .show();
    });

})();

