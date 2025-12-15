Assessment Recommended API
----------------------------

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
An OpenAPI yaml specification for FTR is available in the following [link](https://github.com/OSTrails/FAIR_testing_resource_vocabulary/blob/main/development/api/open_api_description.yaml) including examples and 
method calls.


GET calls
----------------------------
Each of following methods will return metadata of the artifact in JSON-LD, 
following the FAIR-IF Application Profile. The method MUST accept a GET 
string with key/value as in the table below.  The same method MAY accept a JSON 
Body as in Table 1, via HTTP POST. 

| Method        | Parameter   |   Returns                 |
|-------------  |------------ |-------------------------- |
| `/tests/`     | `testid`    | A list with all the test identifiers suported by the tool. When an id is sent, a DCAT record in JSON-LD is returned     |
| `/benchmarks/`| `bmid`      | A list with all the benchmark identifiers suported by the tool. When an id is sent, a DCAT record in JSON-LD is returned     |
| `/metrics/`   | `mid`       | A list with all the metrics identifiers suported by the tool. When an id is sent, a DCAT record in JSON-LD is returned     |
| `/algorithms/`| `aid`       | A list with all the algorithms identifiers suported by the tool. When an id is sent, a DCAT record in JSON-LD is returned     |


POST calls
----------------------------
All post requests must submit a body with the resource to assess as follows:
```
{
 "resource_identifier": "https://w3id.org/example#"
}
```

| Method      | Parameter    |   Returns                |
|-------------|--------------|--------------------------|
|`/assess/test/`|testid and resource_identifier| Test result in JSON-LD |
|`/assess/benchmark/`|bmid and resource_identifier| Test result in JSON-LD |
|`/assess/algorithm/`|algoid and resource_identifier| Test result in JSON-LD |
