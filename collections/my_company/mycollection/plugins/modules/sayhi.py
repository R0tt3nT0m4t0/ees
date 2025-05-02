#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(
        name=dict(type='str', required=False, default='World')
    )

    module = AnsibleModule(argument_spec=module_args)

    result = dict(
        changed=False,
        message=f"Hello {module.params['name']} from Python!"
    )

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
