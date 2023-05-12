#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# DOCUMENTATION, EXAMPLES, and METAL_ssh_key_ARGS are generated by
# ansible_specdoc. Do not edit them directly.

DOCUMENTATION = '''
author: Equinix DevRel Team (@equinix) <support@equinix.com>
description: Manage ssh_keys in Equinix Metal. You can use *id* or *label* to lookup
  a ssh_key. If you want to create new ssh_key, you must provide *name*.
module: metal_ssh_key
notes: []
options:
  id:
    description:
    - UUID of the ssh_key.
    required: false
    type: str
  key:
    description:
    - The public key of the ssh_key.
    required: false
    type: str
  label:
    description:
    - The name of the ssh_key.
    required: false
    type: str
requirements:
- python >= 3
- equinix_metal >= 0.0.1
short_description: Manage ssh_keys in Equinix Metal
'''
EXAMPLES = '''
- name: Create new ssh_key
  hosts: localhost
  tasks:
  - equinix.cloud.metal_ssh_key:
      name: new ssh_key
- name: Create new ssh_key within non - default organization
  hosts: localhost
  tasks:
  - equinix.cloud.metal_ssh_key:
      name: my org ssh_key
      organization_id: a4cc87f9-e00f-48c2-9460-74aa60beb6b0
- name: Remove ssh_key by id
  hosts: localhost
  tasks:
  - equinix.cloud.metal_ssh_key:
      id: eef49903-7a09-4ca1-af67-4087c29ab5b6
      state: absent
- name: Create new ssh_key with non - default billing method
  hosts: localhost
  tasks:
  - equinix.cloud.metal_ssh_key:
      name: newer ssh_key
      payment_method_id: abf49903-7a09-4ca1-af67-4087c29ab343
'''
RETURN = '''
metal_ssh_key:
  description: The module object
  returned: always
  sample:
  - "\n{\n  \"backend_transfer_enabled\": false,\n  \"changed\": false,\n  \"customdata\"\
    : {},\n  \"description\": \"\",\n  \"id\": \"7624f0f7-75b6-4271-bc64-632b80f87de2\"\
    ,\n  \"name\": \"ansible-integration-test-ssh_key-csle6t2y-ssh_key1_renamed\"\
    ,\n  \"organization_id\": \"70c2f878-9f32-452e-8c69-ab15480e1d99\",\n  \"payment_method_id\"\
    : \"845b45a3-c565-47e5-b9b6-a86204a73d29\"\n}\n"
  type: dict
'''

# End of generated documentation

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
        description=['UUID of the ssh_key.'],
    ),
    label=SpecField(
        type=FieldType.string,
        description=['The name of the ssh_key.'],
        editable=True,
    ),
    key=SpecField(
        type=FieldType.string,
        description=['The public key of the ssh_key.'],
        editable=True,
    ),
)


specdoc_examples = [
    '''
- name: Create new ssh_key
  hosts: localhost
  tasks:
  - equinix.cloud.metal_ssh_key:
      name: "new ssh_key"
''', '''
- name: Create new ssh_key within non - default organization
  hosts: localhost
  tasks:
  - equinix.cloud.metal_ssh_key:
      name: "my org ssh_key"
      organization_id: "a4cc87f9-e00f-48c2-9460-74aa60beb6b0"
''', '''
- name: Remove ssh_key by id
  hosts: localhost
  tasks:
  - equinix.cloud.metal_ssh_key:
      id: "eef49903-7a09-4ca1-af67-4087c29ab5b6"
      state: absent
''', '''
- name: Create new ssh_key with non - default billing method
  hosts: localhost
  tasks:
  - equinix.cloud.metal_ssh_key:
      name: "newer ssh_key"
      payment_method_id: "abf49903-7a09-4ca1-af67-4087c29ab343"
''',
]

result_sample = ['''
{
  "backend_transfer_enabled": false,
  "changed": false,
  "customdata": {},
  "description": "",
  "id": "7624f0f7-75b6-4271-bc64-632b80f87de2",
  "name": "ansible-integration-test-ssh_key-csle6t2y-ssh_key1_renamed",
  "organization_id": "70c2f878-9f32-452e-8c69-ab15480e1d99",
  "payment_method_id": "845b45a3-c565-47e5-b9b6-a86204a73d29"
}
''']

MUTABLE_ATTRIBUTES = [
    k for k, v in module_spec.items() if v.editable
]

SPECDOC_META = getSpecDocMeta(
    short_description='Manage ssh_keys in Equinix Metal',
    description=(
        'Manage ssh_keys in Equinix Metal. '
        'You can use *id* or *label* to lookup a ssh_key. '
        'If you want to create new ssh_key, you must provide *name*.'
    ),
    examples=specdoc_examples,
    options=module_spec,
    return_values={
        "metal_ssh_key": SpecReturnValue(
            description='The module object',
            type=FieldType.dict,
            sample=result_sample,
        ),
    },
)


def main():
    module = EquinixModule(
        argument_spec=SPECDOC_META.ansible_spec,
        required_one_of=[("label", "id")],
        required_together=[("label", "key")],
    )

    state = module.params.get("state")
    changed = False

    try:
        module.params_syntax_check()
        if module.params.get("id"):
            tolerate_not_found = state == "absent"
            fetched = module.get_by_id("metal_ssh_key", tolerate_not_found)
        else:
            fetched = module.get_one_from_list(
                "metal_ssh_key",
                ["key"],
            )

        if fetched:
            module.params['id'] = fetched['id']
            if state == "present":
                diff = get_diff(module.params, fetched, MUTABLE_ATTRIBUTES)
                if diff:
                    fetched = module.update_by_id(diff, "metal_ssh_key")
                    changed = True

            else:
                module.delete_by_id("metal_ssh_key")
                changed = True
        else:
            if state == "present":
                fetched = module.create("metal_ssh_key")
                changed = True
            else:
                fetched = {}
    except Exception as e:
        tb = traceback.format_exc()
        module.fail_json(msg="Error in metal_ssh_key: {0}".format(to_native(e)),
                         exception=tb)

    fetched.update({'changed': changed})
    module.exit_json(**fetched)


if __name__ == '__main__':
    main()
