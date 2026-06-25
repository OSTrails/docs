.. _run-existing-test:
How to run an existing Test
==============================

Using the FAIR Champion GUI:

https://tools.ostrails.eu/champion/tests/

1. Search (using the browser text search) for the test you want to execute.
2. Click "Execute Text" - this will trigger the creation of a form appropriate for that test
3. Fill-in the form field(s)
4. Click "Run Test"

Alternatively, if you want to automate many executions, you can:

1. a. Use the GUI to find the test (e.g. "fc_data_identifier_in_metadata")
2. a. Right-click on the blue test title and "copy Link" (this is necessary because clicking the link might follow a content-negotiated path to a nice web page, rather than giving you the identifier of the test!)

OR

1. b. Use FAIRSharing to find the Metric that interests you
2. b. Identify a test on the FAIRSharing page that implements that Metric

3. Prepare your input, in the format:  { "resource_identifier": "GUID" }
4. use the code example in the top of that Web page, together with your Test identifier and your input

  curl -H "Content-type: application/json" -H "Accept: application/json"
        -d '{"resource_identifier": "https://exampledataset.org"}'
        https://tests.ostrails.eu/tests/fc_data_identifier_in_metadata

