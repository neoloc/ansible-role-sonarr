# Sonarr role

[![CI](https://github.com/coaxial/ansible-role-sonarr/actions/workflows/ci.yml/badge.svg)](https://github.com/coaxial/ansible-role-sonarr/actions/workflows/ci.yml)

Galaxy: https://galaxy.ansible.com/coaxial/sonarr

## Instructions

This role will install Sonarr and (optionally) install and configure NGINX to
server the UI at `<server address>/sonarr`.

## Variables and their defaults

| variable name       | default value | description                                                                             |
| ------------------- | ------------- | --------------------------------------------------------------------------------------- |
| sonarr\_\_use_nginx | `yes`         | Whether to install and configure nginx (`no` if you're installing/managing it yourself) |
