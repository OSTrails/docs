pyFAT
^^^^^

pyFAT is a FAIR assessment tool, that was originally developed under CLARIAH-NL. 
It was recently updated to be compliant to the FAIR Reference Model defined by OSTrails. 
It adheres to the FAIR Testing Resource Vocabulary (`FTR <https://w3id.org/ftr#>`_) 
and FAIR Guidance Vocabulary (`FGV <https://w3id.org/fgv#>`_) ontologies developed within OSTrails. 
It uses path expressions to traverse meta-data records and do the assessment. 
The metrics and Tests are never hardcoded in PyFAT itself, and it is thus possible 
to specify tests for any metadata format. Currently it is setup to test metadata 
records formatted in CLARIN's Component Metadata Infrastructure (CMDI).

In this release, which is still in beta, pyFAT is able to register tests in FAIR Champion, 
because the test generates a metadata descriptor compliant with the FAIR Reference Model defined by OSTrails.

    - **Code repository**: https://github.com/knaw-huc/ost-pyfat-api
    - **Version**: Release v0.1
    - **Release**: https://pyfat.sd.di.huc.knaw.nl/docs#
    - **License**: MIT


