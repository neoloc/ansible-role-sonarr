import os
import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_sonarr_service(host):
    s = host.service('sonarr')

    assert s.is_enabled
    assert s.is_running


def test_sonarr_http(host):
    html = host.run('curl http://localhost/sonarr').stdout

    assert 'Sonarr' in html


def test_sonarr_base_url(host):
    html = host.run('curl http://localhost/sonarr').stdout

    assert '/sonarr/favicon.ico' in html


def test_sonarr_config_file(host):
    f = host.file('/var/lib/sonarr/config.xml')
    c = re.compile(
        r"<Config>.*<UrlBase>/sonarr</UrlBase>.*</Config>",
        flags=re.DOTALL
    )

    assert re.match(c, f.content_string)


def test_firewall(host):
    i = host.iptables

    assert (
        '-A INPUT -p tcp -m tcp --dport 80 '
        '-m conntrack --ctstate NEW,ESTABLISHED '
        '-m comment --comment "Allow HTTP traffic" -j ACCEPT'
    ) in i.rules('filter', 'INPUT')
    assert (
        '-A OUTPUT -p tcp -m tcp --sport 80 '
        '-m conntrack --ctstate ESTABLISHED '
        '-m comment --comment "Allow HTTP traffic" -j ACCEPT'
    ) in i.rules('filter', 'OUTPUT')


def test_mono_repo(host):
    f = host.file("/etc/apt/sources.list.d/mono-official-stable.list")

    f.exists


def test_mediaarea_repo(host):
    f = host.file("/etc/apt/sources.list.d/mediaarea.list")

    f.exists


def test_sonarr_group(host):
    u = host.user('sonarr')

    assert 'media' in u.groups
