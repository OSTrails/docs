:orphan:

.. _tool-fair-algorithms:

FAIR Algorithms
===============

The algorithms below are maintained as live endpoints by the OSTrails project together with private partners who are committed to maintaining the testing infrastructure.
Algorithms are catalogued in the :ref:`OSTrails Software Tools Registry <software-registry>`, which provides the listing below via an API call.
All algorithms are compliant with the `FTR Vocabulary <https://w3id.org/ftr>`_ and can be executed through the platforms described under :ref:`tool-testing-platforms`.

Use the search box to filter by algorithm name or description.

.. raw:: html

   (A static JSON snapshot of the algorithm catalogue is <a href="https://github.com/OSTrails/docs/static_data_dumps/algos.json">here</a>: dumped on July 17, 2026.)

   <style>
   .catalog-search {
     width: 100%;
     padding: 8px 12px;
     margin-bottom: 16px;
     font-size: 14px;
     border: 1px solid #ccc;
     border-radius: 4px;
     box-sizing: border-box;
     display: none;
   }
   .catalog-count {
     font-size: 0.9em;
     color: #555;
     margin-bottom: 10px;
   }
   .catalog-card {
     border: 1px solid #dde0e4;
     border-radius: 4px;
     margin-bottom: 6px;
   }
   .catalog-card > summary {
     padding: 9px 14px;
     cursor: pointer;
     background: #f5f7fa;
     border-radius: 4px;
     list-style: none;
     user-select: none;
   }
   .catalog-card > summary::-webkit-details-marker { display: none; }
   .catalog-card[open] > summary {
     background: #e8eef8;
     border-bottom: 1px solid #dde0e4;
     border-radius: 4px 4px 0 0;
   }
   .catalog-body {
     padding: 10px 16px 12px 16px;
   }
   .catalog-body p { margin: 0 0 8px 0; }
   .catalog-body dl { margin: 6px 0 0 0; }
   .catalog-body dt {
     font-weight: 600;
     margin-top: 6px;
     color: #333;
   }
   .catalog-body dd {
     margin: 2px 0 0 0;
     word-break: break-all;
     font-size: 0.92em;
   }
   </style>

   <input type="text" id="fair-algorithms-search" class="catalog-search" placeholder="Filter algorithms by name or description…">
   <div id="fair-algorithms-count" class="catalog-count"></div>
   <div id="fair-algorithms-container"><em>Loading FAIR algorithm catalogue…</em></div>

   <script>
   (function () {
     function esc(s) {
       return String(s)
         .replace(/&/g, '&amp;')
         .replace(/</g, '&lt;')
         .replace(/>/g, '&gt;')
         .replace(/"/g, '&quot;');
     }

     var container = document.getElementById('fair-algorithms-container');
     var searchBox = document.getElementById('fair-algorithms-search');
     var countEl  = document.getElementById('fair-algorithms-count');

     fetch('https://w3id.org/FAIR-Champion/algorithms/', {
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
           '<details class="catalog-card">',
           '<summary><strong>' + esc(t.title) + '</strong></summary>',
           '<div class="catalog-body">',
           '<p>' + esc(t.description) + '</p>',
           '<dl>',
           '<dt>Identifier</dt>',
           '<dd><a href="' + esc(t.identifier) + '">' + esc(t.identifier) + '</a></dd>',
           '<dt>Algorithm endpoint</dt>',
           '<dd><a href="' + esc(t.endpoint) + '">' + esc(t.endpoint) + '</a></dd>',
           '<dt>API documentation</dt>',
           '<dd><a href="' + esc(t.openapi) + '">OpenAPI specification</a></dd>',
           '</dl>',
           '</div>',
           '</details>'
         ].join('\n');
       });

       container.innerHTML = cards.join('\n');
       countEl.textContent = tests.length + ' algorithms';
       searchBox.style.display = '';

       searchBox.addEventListener('input', function () {
         var q = this.value.toLowerCase();
         var all = container.querySelectorAll('.catalog-card');
         var visible = 0;
         all.forEach(function (card) {
           var match = !q || card.textContent.toLowerCase().indexOf(q) !== -1;
           card.style.display = match ? '' : 'none';
           if (match) visible++;
         });
         countEl.textContent = (q ? visible + ' of ' + all.length : all.length) + ' algorithms';
       });
     })
     .catch(function (e) {
       container.innerHTML =
         '<p><strong>Unable to load the live algorithm catalogue.</strong> ' +
         'You can <a href="https://tools.ostrails.eu/champion/algorithms/">browse the API directly</a>.</p>';
       console.error('FAIR algorithms fetch failed:', e);
     });
   })();
   </script>
