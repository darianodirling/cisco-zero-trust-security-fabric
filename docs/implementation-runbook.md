# Implementation and rollback runbook

## Preflight
- [ ] Architecture and data flows approved by owners.
- [ ] Release, hardware, license and feature compatibility documented.
- [ ] Config backups and out-of-band access verified.
- [ ] AD/ISE certificate, DNS, NTP and RADIUS dependencies validated.
- [ ] Firewall policy and SGT matrix reviewed for hidden dependencies.
- [ ] Change window, maintenance contacts and rollback thresholds agreed.

## Phased deployment
1. Establish telemetry baselines and backup device configs.
2. Pilot 802.1X/EAP-TLS with a small managed endpoint cohort.
3. Validate ISE authorization, CoA and failure handling.
4. Implement FTD policies in monitored staging; test legitimate flows.
5. Restrict ASA VPN landing-zone traffic and test MFA.
6. Validate Cisco Secure Access policies with managed and unmanaged devices.
7. Enable TrustSec propagation only on confirmed compatible platforms.
8. Run positive and negative access tests, capture evidence and obtain signoff.

## Rollback
1. Halt further rollout and notify incident/change owner.
2. Restore last known-good approved firewall/access policies.
3. Revert affected switch authentication policies using OOB access if needed.
4. Validate identity, routing, remote access and application availability.
5. Record incident timeline, impacted services and follow-up actions.
