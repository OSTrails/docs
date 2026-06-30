.. _deploy-champion:

How to deploy Champion myself
===============================

You only need to do this if you are testing records that are, for example, behind a firewall.  Most of the time you
will simply go to `Champion <https://tools.ostrails.eu/champion>`_

If you feel the need to checkout the code, go to:
https://github.com/OSTrails/FAIR-Champion/

However, you can simply access the latest Docker image, using the following docker-compose file:

    services:

      champion:
        image: markw/fair-champion:0.3.0
          environment:
            - TESTHOST=https://tests.ostrails.eu/tests/
            - CHAMPHOST=http://localhost:8383/
        ports:
            - "8383:4567"


      swagger-converter:
        image: swaggerapi/swagger-converter:latest
        container_name: swagger-converter

Find the latest versioned tag for Champion at `Dockerhub <https://hub.docker.com/repository/docker/markw/fair-champion/tags>`_

The following environment variables should be set (in the docker-compose, probably)


    RACK_ENV='development'

    TEST_HOST='https://tests.ostrails.eu/tests' # this is probably now deprecated, as per March 2026

    CHAMP_HOST=https://tools.ostrails.eu/champion' # the URL of your own Champion instance

    FDPINDEX_SPARQL='https://tools.ostrails.eu/repositories/fdpindex-fdp'  # THIS IS CRITICAL!

    FDPINDEXPROXY='https://tools.ostrails.eu/fdp-index-proxy/proxy' # if you plan to regisgter new tests or benchmarks using your local copy

    CHAMPION_HOST='https://tools.ostrails.eu/champion'  # probably redundant to the one above.  I'll check


That's all!
