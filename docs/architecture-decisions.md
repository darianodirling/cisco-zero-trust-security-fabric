# Architecture decisions

## ADR-001: Identity as an input, not the sole control
**Decision:** Use AD and ISE for user/device identity, but enforce segmentation on supported switches/firewalls. **Tradeoff:** Extra integration complexity; better containment.

## ADR-002: FTD/FMC as interzone enforcement
**Decision:** Route sensitive interzone flows through FTD managed by FMC. **Tradeoff:** Adds latency/capacity and HA requirements; provides policy centralization and audit.

## ADR-003: ASA VPN landing zone
**Decision:** Terminate remote VPN access into a restricted segment with MFA and least-privilege access. **Tradeoff:** Requires separate VPN lifecycle management and operational monitoring.

## ADR-004: TrustSec and pxGrid integration
**Decision:** Use ISE-assigned SGTs and share context with supported consumers. **Tradeoff:** Requires platform-specific support validation and fallback design; pxGrid itself does not enforce policy.

## Release validation gate
Record IOS XE/ASA/FTD/FMC/ISE/Secure Access versions, licenses, compatibility, HA model, support lifecycle, API capabilities and approved rollback plans before implementation.
