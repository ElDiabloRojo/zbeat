# Grafana

This directory contains the required provisions for deploying Grafana as part 
of the local development stack.

# Provisioning

Grafana's active provisioning system allows data sources and dashboards can to 
be specified using config files.

* [Provisioning](./provisioning/README.md)

# Environment Config

The environmental config supplied to the grafana container can be found in the
file [config.monitoring](./config.monitoring), see more about grafana
environment variables [here](https://grafana.com/docs/grafana/latest/administration/configuration/#configure-with-environment-variables).