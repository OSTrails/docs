Assessment Recommended API
==========================

The FAIR-IF follows, as closely as possible, the REST standard;
however, unlike many REST architectures, not all identifiers in
the IF are “local”, and thus it is often necessary to pass the
full GUID of an identifier from one component to another, or from
client to server.  For example, the GUID of a Benchmark is the
DOI of that Benchmark as recorded in the FAIRsharing registry,
and as such, it cannot become part of the URL of the REST interface.

Nevertheless, there are two “types” of calls in the FAIR-IF.
Calls that are intended to retrieve information and calls that are
intended to trigger an activity (such as a test or assessment).
The latter kinds of calls are prefixed with /assess/.

Please refer to the paragraphs below for API calls or implementation.
An OpenAPI yaml specification for FTR is available in the following `link <https://github.com/OSTrails/FAIR_testing_resource_vocabulary/blob/main/development/api/open_api_description.yaml>`_ including examples and
method calls.


GET calls
---------

Each of following methods will return metadata of the artifact in JSON-LD,
following the FAIR-IF Application Profile. The method MUST accept a GET
string with key/value as in the table below.  The same method MAY accept a JSON
Body as in Table 1, via HTTP POST.

.. list-table:: GET endpoints
    :header-rows: 1
    :widths: 20 20 60

    * - Method
      - Parameter
      - Returns
    * - ``/tests/``
      - ``testid``
      - A list with all the test identifiers supported by the tool.
        When an id is sent, a DCAT record in JSON-LD is returned.
    * - ``/benchmarks/``
      - ``bmid``
      - A list with all the benchmark identifiers supported by the tool.
        When an id is sent, a DCAT record in JSON-LD is returned.
    * - ``/metrics/``
      - ``mid``
      - A list with all the metrics identifiers supported by the tool.
        When an id is sent, a DCAT record in JSON-LD is returned.
    * - ``/algorithms/``
      - ``aid``
      - A list with all the algorithms identifiers supported by the tool.
        When an id is sent, a DCAT record in JSON-LD is returned.

POST calls
----------

All post requests must submit a body with the resource to assess as follows:

.. code-block:: json

    {
        "resource_identifier": "https://w3id.org/example#"
    }

.. list-table:: POST endpoints
    :header-rows: 1
    :widths: 20 20 60

    * - Method
      - Parameter
      - Returns
    * - ``/assess/test/``
      - ``testid`` and ``resource_identifier``
      - Test result in JSON-LD
    * - ``/assess/benchmark/``
      - ``bmid`` and ``resource_identifier``
      - Test result in JSON-LD
    * - ``/assess/algorithm/``
      - ``algoid`` and ``resource_identifier``
      - Test result in JSON-LD

In some cases, FAIR assessments may require inspecting multiple large resources. This is, for example, the case when assessing Research Objects. In such situations, the API may not immediately return the test results in JSON-LD format. Instead, it returns a JSON response with the following information:

.. code-block:: json

    {
      "ticket_id": "<ID of the response>"
    }

In this case, the API returns an HTTP status code **202 (Accepted)**, indicating that the assessment request has been successfully created. Additionally, the response header **Location** contains a link where the results will be available once generated.

The link follows this format::

    /assess/algorithm/{ticket_id}

When accessing this link, you may receive one of the following HTTP status codes:

- **404 (Not Found)** if the results have not yet been generated
- **200 (OK)** if the results are available, returned in the same JSON-LD format as a standard test result
