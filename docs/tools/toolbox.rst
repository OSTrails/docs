OSTrails DELIVERABLE 3.2: Toolbox of Testing Services
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The OSTrails Interoperability Framework defines a variety of digital objects that represent
the conceptual and code-level artefacts in the assessment space.  At the conceptual level
are Metrics and Benchmarks.  At the code level are Tests and Algorithms.

It is also important to distinguish between the code of a service and its deployment as an active endpoint.
Generally speaking, DMP tests are provided as code-level objects in the project GitHub and do not
exist as public services.  In the case of FAIR tests, these have been adopted by a commercial entity
and will be updated and maintained as active endpoints beyond the end of the OSTrails project.  As such,
the lists of Tests below differs slightly between the DMP Tests (code) and the FAIR Tests (active endpoints).
Both FAIR tests and DMP tests are compliant with the FTR Vocabulary, and are thus interoperable.

.. toctree::
    :caption: Core Components
    :maxdepth: 1
    :titlesonly:

    Metrics and Benchmarks <conceptual/metrics-and-benchmarks>
    Tests and Algorithms <code/tests-and-algorithms>

.. toctree::
    :caption: Testing Platforms
    :maxdepth: 1
    :titlesonly:

    FAIR Testing Platforms <fair>
    DMP Assessment Platforms <dmp>
    SKG Assesment Platforms <skg>


In addition to testing and assessment tools, 
the OSTrails project has also developed a number of other tools 
that support the testing ecosystem.  
These include:   

.. toctree::
    :caption: Registries
    :maxdepth: 1
    :titlesonly:

    FAIRassist (Conceptual Component Registry) <authoring-and-registering/fairassist>
    OSTrails Software Tools Index <authoring-and-registering/ostrails-index>


.. toctree::
    :caption: Supporting Tools
    :maxdepth: 1
    :titlesonly:

    Assessment Authoring and Registration Tools<authoring>
    Validation and Quality Control Tools<quality-control>

.. toctree::
    :caption: APIs
    :maxdepth: 1
    :titlesonly:

    CESSDA API<apis/cessda>
    OpenAIRE API<apis/openaire>
    RO-Hub API<apis/rohub>

