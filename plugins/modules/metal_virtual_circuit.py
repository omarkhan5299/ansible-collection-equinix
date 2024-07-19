#!/usr/bin/python
# -*- coding: utf-8 -*-
from equinix_metal.exceptions import NotFoundException

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# DOCUMENTATION, EXAMPLES, and RETURN are generated by
# ansible_specdoc. Do not edit them directly.

DOCUMENTATION = r"""
author: Equinix DevRel Team (@equinix) <support@equinix.com>
description: Manage a Virtual Circuit in Equinix Metal. You can use *id* or *name*
  to lookup the resource. If you want to create new resource, you must provide *name*.
module: metal_virtual_circuit
notes: []
options:
  connection_id:
    description:
    - UUID of Connection where the VC is scoped to.
    required: false
    type: str
  customer_ip:
    description:
    - The Customer IP address which the CSR switch will peer with.
    - Will default to the other usable IP in the subnet.
    required: false
    type: str
  description:
    description:
    - Description for the Virtual Circuit resource.
    required: false
    type: str
  id:
    description:
    - UUID of the Virtual Circuit.
    required: false
    type: str
  md5:
    description:
    - The password that can be set for the VRF BGP peer
    required: false
    type: str
  metal_ip:
    description:
    - The Metal IP address for the SVI (Switch Virtual Interface) of the VirtualCircuit.
    - Will default to the first usable IP in the subnet.
    required: false
    type: str
  name:
    description:
    - Name of the Virtual Circuit resource.
    required: false
    type: str
  nni_vlan:
    description:
    - Equinix Metal network-to-network VLAN ID.
    required: false
    type: int
  peer_asn:
    description:
    - The BGP ASN of the peer.
    - The same ASN may be the used across several VCs, but it cannot be the same as
      the local_asn of the VRF.
    required: false
    type: int
  port_id:
    description:
    - UUID of the Connection Port where the VC is scoped to.
    required: false
    type: str
  project_id:
    description:
    - UUID of the Project where the VC is scoped to.
    required: false
    type: str
  speed:
    description:
    - Speed of the Virtual Circuit resource.
    required: false
    type: str
  subnet:
    description:
    - A subnet from one of the IP blocks associated with the VRF that we will help
      create an IP reservation for.
    - Can only be either a /30 or /31.
    - For a /31 block, it will only have two IP addresses, which will be used for
      the metal_ip and customer_ip.
    - For a /30 block, it will have four IP addresses, but the first and last IP addresses
      are not usable.
    - We will default to the first usable IP address for the metal_ip.
    required: false
    type: str
  tags:
    description:
    - Tags for the Virtual Circuit resource.
    required: false
    type: str
  timeout:
    default: 15
    description:
    - Timeout in seconds for Virtual Circuit to get to "ready" state
    required: false
    type: int
  vlan_id:
    description:
    - UUID of the VLAN to associate.
    required: false
    type: str
  vnid:
    description:
    - VNID VLAN parameter, see the documentation for Equinix Fabric.
    required: false
    type: str
  vrf:
    description:
    - UUID of the VRF to associate.
    required: false
    type: str
requirements: null
short_description: Manage a Virtual Circuit in Equinix Metal
"""
EXAMPLES = r"""
- name: create first VRF virtual circuit for test
  hosts: localhost
  tasks:
  - equinix.cloud.metal_virtual_circuit:
      connection_id: 52373d96-ac4e-496c-8721-f7ef18a01331
      port_id: 52373d96-ac4e-496c-8721-f7ef18a01331
      name: test_virtual_circuit
      nni_vlan: 1056
      peer_asn: 66000
      project_id: 11e047e1-f51a-49c6-b5b2-1c7bfa4391e6
      subnet: 192.168.151.126/31
      vrf: 029c4219-04b7-4992-9fef-29ea7e2378a5
"""
RETURN = r"""
metal_virtual_circuit:
  description: The module object
  returned: always
  sample:
  - changed: false
    customer_ip: 192.168.151.127
    id: 84f35a2f-1e0c-43ee-bd94-87aec0c5ffec
    metal_ip: 192.168.151.126
    name: test_virtual_circuit
    nni_vlan: 1056
    peer_asn: 66000
    port:
      href: /metal/v1/connections/52373d96-ac4e-496c-8721-f7ef18a01331/ports/52373d96-ac4e-496c-8721-f7ef18a01331
      id: 4632fb7b-b1cf-48bc-8f20-a69b0a91d326
    project:
      href: /metal/v1/projects/11e047e1-f51a-49c6-b5b2-1c7bfa4391e6
      id: 11e047e1-f51a-49c6-b5b2-1c7bfa4391e6
    project_id: 11e047e1-f51a-49c6-b5b2-1c7bfa4391e6
    status: active
    subnet: 192.168.151.126/31
    tags: []
    type: vrf
    vrf:
      bill: false
      href: /metal/v1/vrfs/029c4219-04b7-4992-9fef-29ea7e2378a5
      id: 029c4219-04b7-4992-9fef-29ea7e2378a5
  type: dict
"""

# End of generated documentation

# This is a template for a new module. It is not meant to be used as is.
# It is meant to be copied and modified to create a new module.
# Replace all occurrences of "metal_resource" with the name of the new
# module, for example "metal_vlan".


from ansible.module_utils._text import to_native
from ansible_specdoc.objects import (
    SpecField,
    FieldType,
    SpecReturnValue,
)
import traceback

from ansible_collections.equinix.cloud.plugins.module_utils.equinix import (
    EquinixModule,
    get_diff,
    getSpecDocMeta,
)


module_spec = dict(
    id=SpecField(
        type=FieldType.string,
        description=['UUID of the Virtual Circuit.'],
    ),
    name=SpecField(
        type=FieldType.string,
        description=['Name of the Virtual Circuit resource.'],
        editable=True,
    ),
    connection_id=SpecField(
        type=FieldType.string,
        description=[
            'UUID of Connection where the VC is scoped to.'
        ],
    ),
    project_id=SpecField(
        type=FieldType.string,
        description=[
            'UUID of the Project where the VC is scoped to.'
        ],
    ),
    port_id=SpecField(
        type=FieldType.string,
        description=[
            'UUID of the Connection Port where the VC is scoped to.'
        ],
    ),
    nni_vlan=SpecField(
        type=FieldType.integer,
        description=[
            'Equinix Metal network-to-network VLAN ID.'
        ],
    ),
    vlan_id=SpecField(
       type=FieldType.string,
       description=[
           'UUID of the VLAN to associate.'
       ],
    ),
    vnid=SpecField(
       type=FieldType.string,
       description=[
           'VNID VLAN parameter, see the documentation for Equinix Fabric.'
       ],
    ),
    description=SpecField(
        type=FieldType.string,
        description=[
            'Description for the Virtual Circuit resource.'
        ],
    ),
    tags=SpecField(
        type=FieldType.string,
        description=[
            'Tags for the Virtual Circuit resource.'
        ],
    ),
    speed=SpecField(
        type=FieldType.string,
        description=[
            'Speed of the Virtual Circuit resource.'
        ],
    ),
    vrf=SpecField(
        type=FieldType.string,
        description=[
            'UUID of the VRF to associate.'
        ],
    ),
    peer_asn=SpecField(
        type=FieldType.integer,
        description=[
            'The BGP ASN of the peer.',
            'The same ASN may be the used across several VCs, but it cannot be the same as the local_asn of the VRF.'
        ],
    ),
    subnet=SpecField(
        type=FieldType.string,
        description=[
            'A subnet from one of the IP blocks associated with the VRF that we will help create an IP reservation for.',
            'Can only be either a /30 or /31.',
            'For a /31 block, it will only have two IP addresses, which will be used for the metal_ip and customer_ip.',
            'For a /30 block, it will have four IP addresses, but the first and last IP addresses are not usable.',
            'We will default to the first usable IP address for the metal_ip.',
        ],
    ),
    metal_ip=SpecField(
        type=FieldType.string,
        description=[
            'The Metal IP address for the SVI (Switch Virtual Interface) of the VirtualCircuit.',
            'Will default to the first usable IP in the subnet.'
        ],
    ),
    customer_ip=SpecField(
        type=FieldType.string,
        description=[
            'The Customer IP address which the CSR switch will peer with.',
            'Will default to the other usable IP in the subnet.'
        ],
    ),
    md5=SpecField(
        type=FieldType.string,
        description=[
            'The password that can be set for the VRF BGP peer'
        ],
    ),
    timeout=SpecField(
        type=FieldType.integer,
        description=[
            'Timeout in seconds for Virtual Circuit to get to "ready" state'
        ],
        default=15,
    ),
)

specdoc_examples = [
    '''
- name: create first VRF virtual circuit for test
  hosts: localhost
  tasks:
  - equinix.cloud.metal_virtual_circuit:
      connection_id: "52373d96-ac4e-496c-8721-f7ef18a01331"
      port_id: "52373d96-ac4e-496c-8721-f7ef18a01331"
      name: "test_virtual_circuit"
      nni_vlan: 1056
      peer_asn: 66000
      project_id: "11e047e1-f51a-49c6-b5b2-1c7bfa4391e6"
      subnet: "192.168.151.126/31"
      vrf: "029c4219-04b7-4992-9fef-29ea7e2378a5"
''',
]

return_values = [
    {
        "changed": False,
        "customer_ip": "192.168.151.127",
        "id": "84f35a2f-1e0c-43ee-bd94-87aec0c5ffec",
        "metal_ip": "192.168.151.126",
        "name": "test_virtual_circuit",
        "nni_vlan": 1056,
        "peer_asn": 66000,
        "port": {
            "href": "/metal/v1/connections/52373d96-ac4e-496c-8721-f7ef18a01331/ports/52373d96-ac4e-496c-8721-f7ef18a01331",
            "id": "4632fb7b-b1cf-48bc-8f20-a69b0a91d326"
        },
        "project": {
            "href": "/metal/v1/projects/11e047e1-f51a-49c6-b5b2-1c7bfa4391e6",
            "id": "11e047e1-f51a-49c6-b5b2-1c7bfa4391e6"
        },
        "project_id": "11e047e1-f51a-49c6-b5b2-1c7bfa4391e6",
        "status": "active",
        "subnet": "192.168.151.126/31",
        "tags": [],
        "type": "vrf",
        "vrf": {
            "bill": False,
            "href": "/metal/v1/vrfs/029c4219-04b7-4992-9fef-29ea7e2378a5",
            "id": "029c4219-04b7-4992-9fef-29ea7e2378a5"
        }
    }
]

MUTABLE_ATTRIBUTES = [
    k for k, v in module_spec.items() if v.editable
]

SPECDOC_META = getSpecDocMeta(
    short_description='Manage a Virtual Circuit in Equinix Metal',
    description=(
        'Manage a Virtual Circuit in Equinix Metal. '
        'You can use *id* or *name* to lookup the resource. '
        'If you want to create new resource, you must provide *name*.'
    ),
    examples=specdoc_examples,
    options=module_spec,
    return_values={
        "metal_virtual_circuit": SpecReturnValue(
            description='The module object',
            type=FieldType.dict,
            sample=return_values,
        ),
    },
)


def main():
    module = EquinixModule(
        argument_spec=SPECDOC_META.ansible_spec,
    )

    state = module.params.get("state")
    changed = False
    module_route = 'metal_virtual_circuit_vrf' if module.params.get('vrf', False) else 'metal_virtual_circuit'

    try:
        module.params_syntax_check()
        fetched = None
        if module.params.get("id"):
            tolerate_not_found = state == "absent"
            fetched = module.get_by_id(module_route, tolerate_not_found)
        else:
            fetched = module.get_one_from_list(
                module_route,
                ["name"],
            )

    except NotFoundException as e:
        pass

    except Exception as e:
        tb = traceback.format_exc()
        module.fail_json(msg="Error in metal_virtual_circuit: {0}".format(to_native(e)),
                         exception=tb)

    try:
        if fetched:
            module.params['id'] = fetched['id']
            if state == "present":
                diff = get_diff(module.params, fetched, MUTABLE_ATTRIBUTES)
                if diff:
                    fetched = module.update_by_id(diff, module_route)
                    changed = True

            else:
                module.delete_by_id(module_route)

                module.wait_for_resource_removal(
                    module_route,
                    timeout=module.params.get("timeout"),
                )
                changed = True
        else:
            if state == "present":
                fetched = module.create(module_route)
                if 'id' not in fetched:
                    module.fail_json(msg="UUID not found in resource creation response")
                changed = True
            else:
                fetched = {}

    except Exception as e:
        tb = traceback.format_exc()
        module.fail_json(msg="Error in metal_virtual_circuit: {0}".format(to_native(e)),
                         exception=tb)

    fetched.update({'changed': changed})
    module.exit_json(**fetched)


if __name__ == '__main__':
    main()
