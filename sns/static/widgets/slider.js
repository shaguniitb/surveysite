'use strict';
(function () {
  const INTENSITY_EXAMPLES = {
    'L5': [
      'Banter comes with sports. If you\'re losing sleep over what someone had to say on social media then you have issues. What did you think we weren\'t gonna talk shit? It\'s the softies like you that can\'t take it and go fishing for screenshots.',
      'He is insinuating that Elena Kaigan is an illegal because of her ethnicity? This mofo is lower than a snake\'s belly under a wagon wheel.',
      'IDK who you are but you know good &amp; well that this is a LOADED, misguided, & misleading question. Cut that shit out, knucklehead, you know better. And u know EXACTLY what you\'re doing! 👌🏻'
    ],
    'L4': [
      'Idk why niggas be thinking saying they gone put a baby in a mf is a compliment 😂 I don\'t want no nigga in Madison baby 🗣💯',
      'I heard somewhere that Nadler is a pedophile, and is one of the sexual predators/pedophiles in Congress that used MILLIONS of taxpayer $$$ to settle lawsuits with VICTIMS. #ReleaseTheList',
      'What that you have 20 friends??? Lol loser'
    ],
    'L3': [
      'Project managers don\'t pay people, you dumbass 😂 I guess nobody\'s ever hired you for anything big enough to deal with one. Also, it\'s not my money, so even if payment was my call, why would I care? Are you sure you work in that field?',
      'I\'m not your comrade. "daaaaam" this is not correct English, it is spelled damned. "I am..,,, you really" this is not correct English either. "lol You need a time out." this one is complete retardation. 😀😀😀😀',
      'So that\'s why Eric is the slow ugly one.'
    ],
    'L2': [
      'every fucking week i just wish that asshole that sits near me dies of a heart attack because he has a heart problem',
      'Either by absorption or adsorption, when I cum on your face, part of me will be a part of you for the rest of the day...',
      'Killa 2020 : youse a fucking cunt'
    ],
    'L1': []
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
