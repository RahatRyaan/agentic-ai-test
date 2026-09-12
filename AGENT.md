# Agent Operational Constraints & Permissions

This document specifies the operational permissions, safety boundaries, and engineering constraints for autonomous agents working within this repository and workstation.

---

## 1. Safety & Execution Boundaries

1. **Destructive Operations Prohibited:**
   - Never execute recursive destructive deletions (`rm -rf /`, `rm -rf ~`, or unconstrained wipes).
   - Never force-push (`git push --force`) or hard-reset (`git reset --hard`) tracking branches.
   - Never delete personal keys (`~/.ssh/id_*`) or existing projects.

2. **Credential & Secret Protection:**
   - Never print, log, or commit private keys, API tokens, passwords, or authentication cookies.
   - Never ask the user to enter passwords in unencrypted chat channels.

3. **Least Privilege & Sudo Policy:**
   - Execute project-level scripts, builds, and tests using standard unprivileged user permissions (`rahat-akanda`).
   - Sudo is reserved solely for system-level package management and must be pre-explained to the user.

---

## 2. Engineering & Code Standards

1. **Idempotence & Backups:**
   - Always back up modified configuration files using timestamped extensions (`<file>.bak.<timestamp>`).
   - Scripts and automations must be safe to rerun without creating duplicate state or errors.

2. **Resource Management:**
   - Target machine has 13 GiB RAM and 12 CPU cores. Keep local AI model sizes restricted to lightweight parameter counts (<=4B parameters, e.g. `qwen2.5-coder:3b` or `1.5b`) to avoid OOM killer triggers or swap thrashing.
   - Local microservice containers must bind exclusively to `127.0.0.1`.

3. **Testing & Validation:**
   - Every feature or utility must include automated unit tests runnable locally without network dependencies.
   - Container builds must be validated before deployment.
