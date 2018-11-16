# Knative installer

Simple collection of playbook/roles that provisions knative on an openshift cluster based on its docs: https://github.com/knative/docs/blob/master/install/Knative-with-OpenShift.md

## Running

Everything runs on the local machine.

```sh
#installs everything
ansible-playbook -i inventories/host.cfg playbooks/install-all.yml
#installs istio only
ansible-playbook -i inventories/host.cfg playbooks/install-istio.yml
#installs knative only
ansible-playbook -i inventories/host.cfg playbooks/install-knative.yml
```

## Docs

### Istio

Deploys istio resources: https://storage.googleapis.com/knative-releases/serving/latest/istio.yaml

#### Vars

| name                    | type    | default                      |
| ----------------------- | ------- | ---------------------------- | 
| istio_privileged_mode   | bool    | true                         |
| istio_tmp_folder        | string  | /tmp/knative-installer/istio |
| istio_namespace         | string  | istio-system                 |


### Knative Serving

Deploys knative serving resources: https://storage.googleapis.com/knative-releases/serving/latest/release-lite.yaml

#### Vars

| name                       | type    | default                                 |
| -------------------------- | ------- | --------------------------------------- | 
| knative_serving_tmp_folder | string  | /tmp/knative-installer/knative-servinvg |
| knative_serving_namespace  | string  | istio-system                            |

## License

[Apache License, Version 2.0](LICENSE)
