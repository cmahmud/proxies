# SyndProxy private pool

## Current pool

- Alive now: 969
- Gold now: 379
- HTTP: 333 alive / 86 gold
- HTTPS: 198 alive / 23 gold
- SOCKS4: 211 alive / 124 gold
- SOCKS5: 227 alive / 146 gold

## Historical pool

- Discovered: 163880
- Ever alive: 32039
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
