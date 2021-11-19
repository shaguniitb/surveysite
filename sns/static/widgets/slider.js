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
    'L1': [],
    'L2': [],
    'L3': [],
    'L4': [],
    'L5': [],
  };
  const INTENSITY_EXPLANATIONS = {
    'L1': 'You have set the moderation to "Nothing". No posts will be removed at this level.',
    'L2': 'You have set the moderation to "Very Toxic". At this level, posts that are at the toxicity of "very toxic" will be removed. ',
    'L3': 'You have set the moderation to "Toxic". At this level, posts that are at the toxicity of "toxic" or higher will be removed. ',
    'L4': 'You have set the moderation to "Somewhat Toxic". At this level, posts that are at the toxicity of "somewhat toxic" or higher will be removed. ',
    'L5': 'You have set the moderation to "Mildly Toxic". At this level, posts that are at the toxicity of "mildly toxic" or higher will be removed. ',
  };
  const PROBABILITY_EXPLANATIONS = {
    'L1': 'No posts will be removed at this level.',
    'L2': 'Few posts will be removed at this level.',
    'L3': 'Some posts will be removed at this level.',
    'L4': 'More posts will be removed at this level.',
    'L5': 'Many posts will be removed at this leve.',
  };

  function makeChangeListener(mode, showExamples) {
    return function (e) {
      handleSliderChange(e.target.value, mode, showExamples);
    }
  }

  function handleSliderChange(level, mode, examples) {
    if (mode === 'intensity') {
      var examples = INTENSITY_EXAMPLES;
      var explanations = INTENSITY_EXPLANATIONS;
    } else if (mode === 'probability') {
      var examples = PROBABILITY_EXAMPLES;
      var explanations = INTENSITY_EXPLANATIONS;
    }

    var descDiv = document.getElementById('slider-explanation');
    var examplesDiv = document.getElementById('slider-examples');
    if (typeof descDiv !== 'undefined' && descDiv !== null) {
      descDiv.innerText = explanations['L' + level] +
        '';
    }
    if (typeof examplesDiv !== 'undefined' && examplesDiv !== null) {
      examplesDiv.innerHTML = '';
      if (showExamples) {
        var examplesList = examples['L' + level];
        if (typeof examplesList === 'undefined' || examplesList === null) {
          console.log(mode);
        } else if (examplesList.length === 0) {
          examplesDiv.innerText = '';
        } else {
          examplesList.forEach(function (item, i) {
            var example = document.createElement('div');
            example.className = 'tweet';
            examplesDiv.appendChild(example);
            example.innerText = item;
          });
          descDiv.innerText += 'Here are some examples of additional posts that will be removed at this level:'
        }
      }
    }
  }

  function bindSliders(mode, showExamples) {
    var inputs = document.getElementsByTagName('input');
    for (var i = 0; i < inputs.length; i++) {
      if (inputs[i].type == 'range') {
        inputs[i].addEventListener('change', makeChangeListener(mode, showExamples));
        handleSliderChange(inputs[i].value, mode, showExamples);
        return;
      }
    }
  }

  window.addEventListener('load', function () {
    var modeElem = document.getElementById('slider-mode');
    var examplesElem = document.getElementById('examples-mode');
    var mode = 'intensity';
    var showExamples = (examplesElem !== null &&
      examplesElem.innerText.trim() === 'on');
    if (modeElem !== null) {
      mode = modeElem.innerText.trim();
    }
    // find and bind
    bindSliders(mode, showExamples);
  });
})();
