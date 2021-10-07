 $(function() {
  $('#slider').slider({
    range: "max",
    value: 0,
    step: 1,
    min: 1,
    max: 5,
    slide: function(event, ui) {
      $("#amount1").val("$" + ui.value);
      if (ui.value == 1) {
        $("#message").text("EXAMPLES: 1) In Kansas when I was growing up we were able to get our licenses at 14. Most of the kids in school were farm kids. It was not unusual for the boys driving pickups to school would have gun racks in the back window with guns. Those were the days. 2) i may not wanna say it but just so you know youre never any better than myself when it comes to whatever im capable of doing");
      }
      if (ui.value == 2) {
        $("#message").text(
          "EXAMPLES: 1) Autism is a social disability. To get married you need social skills. 2) Football players grind so hard to get that NFL paycheck and females do everything in they power to ruin a mans life over a weak ahh relationship");
      }
      if (ui.value == 3) {
        $("#message").text("EXAMPLES: 1) Nigel Farage looks like a toad plotting a practical joke. Theresa May looks like a depressed waxwork. Boris Johnson looks like a sheepdog peeping out from under an upturned colander of spaghetti. That sort of thing. @YasmeenSerhan on UK sketch writers! 2) I can't believe some girls are pathetic enough to actually be in a e-relationship 3) White peoples be on Twitter calling us niggers and everything but never get banned or blocked");
      }
      if (ui.value == 4) {
        $("#message").text("EXAMPLES: 1) Dick Eric Swalloswell die or something? I keep seeing these obituary type tweets from all the idiot dims running for President. 2) he look like a bosnian terrorist  😭😭😭😭 3) Pakistanis should stfu your team didn't even reached to semifinal #indiavsNewzealand");
      }
      if (ui.value == 5) {
        $("#message").text("EXAMPLES: 1) why the fuck are you crying? 2) Remind this bitch its about viewer content ! More people watch men play then women ! I have no desire to watch dikes running a ball ⚽️ . Men will always make more 3) Nigga swimming with the piss and throw up off Bourbon?! 🤦");
      }
    }
  });
});