# Threat model

| Threat | Impact | Mitigation | Test |
| --- | --- | --- | --- |
| Stolen user credentials | Unauthorized access | MFA, certificate-based device auth, posture | Simulated unauthorized login |
| Compromised endpoint | Lateral movement | Segmentation and SGT policy | Denied interzone test |
| Guest pivot | Internal compromise | Separate guest zone and deny rules | Guest-to-DB denial |
| VPN credential abuse | Privilege escalation | Restricted landing zone and MFA | VPN access matrix |
| Route leak | Availability/security | BGP filters, max-prefix, explicit peers | Lab route-policy test |
| ISE outage | Access disruption | Redundancy and approved fallback behavior | Controlled failover |
| Policy drift | Excess access | Change review, FMC logs, periodic attestations | Rule audit |

**Trust boundaries:** endpoint/campus, campus/core, remote VPN/enterprise, enterprise/internet, application/database, management/data plane.
