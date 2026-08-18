# SyndProxy private pool

## Current pool

- Alive now: 999
- Gold now: 345
- HTTP: 315 alive / 53 gold
- HTTPS: 203 alive / 14 gold
- SOCKS4: 242 alive / 138 gold
- SOCKS5: 239 alive / 140 gold

## Historical pool

- Discovered: 107067
- Ever alive: 14712
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
