import pytest


def test_firewalld_service_is_stopped_and_disabled(host):
    assert host.service("firewalld").is_running is False
    assert host.service("firewalld").is_enabled is False


def test_selinux_is_permissive(host):
    cmd = host.run("getenforce")
    assert cmd.stdout == 'Permissive\n'


@pytest.mark.parametrize("service", [
    "clam-freshclam",
    "clamd@scan",
])
def test_clamav_services_are_active_and_enabled(host, service):
    assert host.service(service).is_running
    assert host.service(service).is_enabled


def test_zabbix_service_is_active_and_enabled(host):
    assert host.service("zabbix-agent").is_running
    assert host.service("zabbix-agent").is_enabled
