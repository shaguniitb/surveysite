'use strict';
(function () {
  const INTENSITY_EXAMPLES = {
    'L5': [
      'In Kansas when I was growing up we were able to get our licenses at 14. Most of the kids in school were farm kids. It was not unusual for the boys driving pickups to school would have gun racks in the back window with guns. Those were the days.',
      'i may not wanna say it but just so you know youre never any better than myself when it comes to whatever im capable of doing'
    ],
    'L4': [
      'Autism is a social disability. To get married you need social skills.',
      'Football players grind so hard to get that NFL paycheck and females do everything in they power to ruin a mans life over a weak ahh relationship'
    ],
    'L3': [
      'Nigel Farage looks like a toad plotting a practical joke. Theresa May looks like a depressed waxwork. Boris Johnson looks like a sheepdog peeping out from under an upturned colander of spaghetti. That sort of thing. @User on UK sketch writers!',
      'I can\'t believe some girls are pathetic enough to actually be in a e-relationship',
      'White peoples be on Twitter calling us niggers and everything but never get banned or blocked'
    ],
    'L2': [
      'Dick Eric Swalloswell die or something? I keep seeing these obituary type tweets from all the idiot dims running for President.',
      'he look like a bosnian terrorist  😭😭😭😭',
      'Pakistanis should stfu your team didn\'t even reached to semifinal #indiavsNewzealand'
    ],
    'L1': [
      'why the fuck are you crying? 2) ',
      'Remind this bitch its about viewer content ! More people watch men play then women ! I have no desire to watch dikes running a ball ⚽️ . Men will always make more',
      'Nigga swimming with the piss and throw up off Bourbon?! 🤦'
    ]
  };
  const PROBABILITY_EXAMPLES = {
    'L1': [
      'there should be'
    ],
    'L2': [
      'some examples here'
    ],
    'L3': [
      'but there are not'
    ],
    'L4': [
      'so this is just filled with nothing'
    ],
    'L5': [
      'and forever nothing'
    ],
  };

  function makeChangeListener(mode) {
    return function (e) {
      handleSliderChange(e.target.value, mode);
    }
  }

  function handleSliderChange(level, mode) {
    if (mode === 'intensity') {
      var examples = INTENSITY_EXAMPLES;
    } else if (mode === 'probability') {
      var examples = PROBABILITY_EXAMPLES;
    }

    var descDiv = document.getElementById('slider-explanation');
    var examplesDiv = document.getElementById('slider-examples');
    if (typeof descDiv !== 'undefined' && descDiv !== null) {
      descDiv.innerText = 'Slider set to ' + level + '. Here are some examples of comments that will be filtered:';
    }
    if (typeof examplesDiv !== 'undefined' && examplesDiv !== null) {
      examplesDiv.innerHTML = '';
      examples['L' + level].forEach(function (item, i) {
        var example = document.createElement('div');
        example.className = 'tweet';
        examplesDiv.appendChild(example);
        example.innerText = item;
      });
    }
  }

  function bindSliders(mode) {
    var inputs = document.getElementsByTagName('input');
    for (var i = 0; i < inputs.length; i++) {
      if (inputs[i].type == 'range') {
        inputs[i].addEventListener('change', makeChangeListener(mode));
        handleSliderChange(inputs[i].value, mode);
        return;
      }
    }
  }

  window.addEventListener('load', function () {
    var modeElem = document.getElementById('slider-mode');
    var mode = 'intensity';
    if (modeElem !== null) {
      mode = modeElem.innerText.trim();
    }
    // find and bind
    bindSliders(mode);
  });
})();
