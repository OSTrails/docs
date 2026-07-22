How host/deploy a test
=========================

The easiest way is to ask someone from OSTrails WP3 to write the test for you, and host it on the OSTrails Infrastructure.
This helps keep tests quality-controlled, consistent, and with reliable up-time.

If you really want to do it yourself, you need:

1. Understand (or author) the Metric that you are going to test.  **this is a pre-requisite for writing the test!**
2. Access to a server
3. Coding knowledge in any language
4. Understanding of the rules for Linked Data
5. Optimally, you would also use a Linked Data library from your language to reduce errors; however the data structures can simply be templated.
6. Understanding of the FTR Vocabulary, and specifically the pieces related to a TestResult object
7. Understand how to author an OpenAPI Service Descriptor
8. Either understand a DCAT DataService object, or use the Test Wizard to author this object

Tests have two "modalities":

1. A test can consume a GUID, and use normal identifier resolution on that to retrieve metadata
2. A test can consume an uploaded metadata record

The API for option 1 is to consume the following JSON data structure:

.. code-block:: json

    { "resource_identifier": "GUID" }


The API for option 2 is to follow this OpenAPI3 pattern for file upload:

.. code-block:: yaml

    requestBody:
      required: true
      content:
        multipart/form-data:
          schema:
            type: object
            required: [file]
            properties:
              file:
                type: string
                format: binary
                description: The uploaded metadata.
          encoding:
            file:
              contentType: application/json


Test outputs must follow the FTR schema, and at a minimim must include

1. The identifier of the metadata object that was tesated
2. The Metric that is associated with the Test
3. The "value" of the output (pass/fail/indeterminate are the only valid outputs)
4. A reference to the TestExecution, and metadata about that (e.g. test identifier, date, version, etc)

Test outputs may optimally include a reference to a Guidance Object.  Guidance Objects are added during test execution, when a test detects an error.  They are intended to help the metadata author avoid the error.

Guidance Objects are still under development, so are not deeply documented here.
