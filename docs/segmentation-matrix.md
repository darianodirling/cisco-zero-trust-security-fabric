# Segmentation matrix

| Source | Destination | Ports | Decision | Enforcement |
| --- | --- | --- | --- | --- |
| Managed endpoint | Web applications | TCP 443 | Permit with identity/posture | Secure Access / FTD |
| Web tier | App tier | TCP 8443 | Permit | FTD |
| App tier | DB tier | TCP 5432 | Permit | FTD |
| VPN users | Admin jump | TCP 443 | Permit with MFA | ASA landing zone / FTD |
| Guest | Internal networks | Any | Deny | Campus/FTD |
| User endpoints | DB tier | Any | Deny | FTD |
| Unapproved lateral | Internal segments | Any | Deny and log | FTD / TrustSec SGACL |

Before enforcement, inventory DNS, NTP, AD, certificate, backup, monitoring and vulnerability scanning traffic. Explicitly test allowed and denied paths.
