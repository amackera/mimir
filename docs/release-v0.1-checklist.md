# Mimir v0.1 Release Checklist

## 1) Scope lock
- [ ] Confirm v0 scope remains minimal (worker + client + core tools)
- [ ] Defer non-v0 items (Drive/GitHub full indexing/Slack prod rollout)

## 2) Implementation gates
- [ ] Worker boots and registers agent/tools via `Norns`
- [ ] Client ingress works via `NornsClient.send_message`
- [ ] Conversation key flow works for follow-ups

## 3) Knowledge + memory
- [ ] `search_knowledge` works on markdown corpus
- [ ] `remember` persists facts
- [ ] `search_memory` retrieves remembered facts

## 4) Reliability checks
- [ ] End-to-end run succeeds after Norns restart
- [ ] No duplicate side effects from marked tools
- [ ] Errors are visible and diagnosable from Norns run timeline

## 5) Docs + DX
- [ ] README setup/quickstart validated from clean env
- [ ] `docs/design.md` and `docs/v0-plan.md` match implementation
- [ ] Add short demo script walkthrough

## 6) Release
- [ ] Tag `v0.1.0`
- [ ] Add release notes + known gaps
- [ ] Gather first user feedback loop
