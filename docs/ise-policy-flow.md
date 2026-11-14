# Cisco ISE policy flow

```mermaid
flowchart TD
  E[Endpoint connects] --> S[Switch 802.1X]
  S --> R[RADIUS request to ISE]
  R --> C{Identity and certificate valid?}
  C -- No --> Q[Reject or quarantine per approved policy]
  C -- Yes --> P{Posture and group}
  P -- Compliant employee --> A[Authorize employee VLAN / SGT]
  P -- Guest --> G[Guest VLAN / restricted SGT]
  P -- Noncompliant --> Q
  A --> X[Enforcement by supported switch / FTD]
  G --> X
  Q --> X
  R -. Context .-> PX[pxGrid subscribers]
```

**Checks:** EAP-TLS trust chain, RADIUS reachability, device time, AD group lookup, CoA, certificate renewal, ISE node failure, authentication bypass exceptions and audit logs.
