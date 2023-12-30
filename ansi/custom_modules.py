from ansible.module_utils.basic import AnsibleModule


def task(module):
    arg1 = module.params["arg1"]
    if not isinstance(arg1, str):
        module.fail_json()


if __name__ == '__main__':
    module = AnsibleModule(
        argument_spec=dict
            (
            arg1=dict(required=True, type='str')
        )
    )

    result = task(module)
    module.exit_json(failed=False, data=result)
