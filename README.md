Server Role
===========

Configures a basic server based on Fedora with CustomOS settings:

- Sets SELinux to 'Permissive' and disables firewalld service.
- Installs and configures Clam Antivirus and Zabbix client.

Requirements
------------

A Fedora system.

Role Variables
--------------

No parameter default variables are defined for this role.
Static variables like packages list or configuration file settings
can be found in vars/ directory.

Dependencies
------------

This role has no dependencies.

Example Playbook
----------------

```
    - hosts: servers
      roles:
         - { role: iac_ansible-role-server }
```

License
-------

GPL3

Author Information
------------------

