
.. _tool-fair-tests:

FAIR Tests
^^^^^^^^^^

The tests below are maintained as live endpoints by the OSTrails project and catalogued in the OSTrails testing infrastructure.
All tests are compliant with the `FTR Vocabulary <https://w3id.org/ftr>`_ and can be executed through the platforms described in :doc:`<fair>`.

Use the search box to filter by test name or description.

.. raw:: html

   <style>
   #fair-tests-search {
     width: 100%;
     padding: 8px 12px;
     margin-bottom: 16px;
     font-size: 14px;
     border: 1px solid #ccc;
     border-radius: 4px;
     box-sizing: border-box;
     display: none;
   }
   #fair-tests-count {
     font-size: 0.9em;
     color: #555;
     margin-bottom: 10px;
   }
   .fair-test-card {
     border: 1px solid #dde0e4;
     border-radius: 4px;
     margin-bottom: 6px;
   }
   .fair-test-card > summary {
     padding: 9px 14px;
     cursor: pointer;
     background: #f5f7fa;
     border-radius: 4px;
     list-style: none;
     user-select: none;
   }
   .fair-test-card > summary::-webkit-details-marker { display: none; }
   .fair-test-card[open] > summary {
     background: #e8eef8;
     border-bottom: 1px solid #dde0e4;
     border-radius: 4px 4px 0 0;
   }
   .fair-test-body {
     padding: 10px 16px 12px 16px;
   }
   .fair-test-body p { margin: 0 0 8px 0; }
   .fair-test-body dl { margin: 6px 0 0 0; }
   .fair-test-body dt {
     font-weight: 600;
     margin-top: 6px;
     color: #333;
   }
   .fair-test-body dd {
     margin: 2px 0 0 0;
     word-break: break-all;
     font-size: 0.92em;
   }
   </style>

   <input type="text" id="fair-tests-search" placeholder="Filter tests by name or description…">
   <div id="fair-tests-count"></div>
   <div id="fair-tests-container"><em>Loading FAIR test catalogue…</em></div>

   <script>
   (function () {
     function esc(s) {
       return String(s)
         .replace(/&/g, '&amp;')
         .replace(/</g, '&lt;')
         .replace(/>/g, '&gt;')
         .replace(/"/g, '&quot;');
     }

     var container = document.getElementById('fair-tests-container');
     var searchBox = document.getElementById('fair-tests-search');
     var countEl  = document.getElementById('fair-tests-count');

     fetch('https://tools.ostrails.eu/champion/tests/', {
       headers: { 'Accept': 'application/json' }
     })
     .then(function (r) {
       if (!r.ok) throw new Error('HTTP ' + r.status);
       return r.json();
     })
     .then(function (tests) {
       tests.sort(function (a, b) {
         return a.title.localeCompare(b.title);
       });

       var cards = tests.map(function (t) {
         return [
           '<details class="fair-test-card">',
           '<summary><strong>' + esc(t.title) + '</strong></summary>',
           '<div class="fair-test-body">',
           '<p>' + esc(t.description) + '</p>',
           '<dl>',
           '<dt>Identifier</dt>',
           '<dd><a href="' + esc(t.identifier) + '">' + esc(t.identifier) + '</a></dd>',
           '<dt>Test endpoint</dt>',
           '<dd><a href="' + esc(t.endpoint) + '">' + esc(t.endpoint) + '</a></dd>',
           '<dt>API documentation</dt>',
           '<dd><a href="' + esc(t.openapi) + '">OpenAPI specification</a></dd>',
           '</dl>',
           '</div>',
           '</details>'
         ].join('\n');
       });

       container.innerHTML = cards.join('\n');
       countEl.textContent = tests.length + ' tests';
       searchBox.style.display = '';

       searchBox.addEventListener('input', function () {
         var q = this.value.toLowerCase();
         var all = container.querySelectorAll('.fair-test-card');
         var visible = 0;
         all.forEach(function (card) {
           var match = !q || card.textContent.toLowerCase().indexOf(q) !== -1;
           card.style.display = match ? '' : 'none';
           if (match) visible++;
         });
         countEl.textContent = (q ? visible + ' of ' + all.length : all.length) + ' tests';
       });
     })
     .catch(function (e) {
       container.innerHTML =
         '<p><strong>Unable to load the live test catalogue.</strong> ' +
         'You can <a href="https://tools.ostrails.eu/champion/tests/">browse the API directly</a>.</p>';
       console.error('FAIR tests fetch failed:', e);
     });
   })();
   </script>
