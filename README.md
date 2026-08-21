# SyndProxy private pool

## Current pool

- Alive now: 930
- Gold now: 416
- HTTP: 298 alive / 89 gold
- HTTPS: 176 alive / 23 gold
- SOCKS4: 216 alive / 142 gold
- SOCKS5: 240 alive / 162 gold

## Historical pool

- Discovered: 156414
- Ever alive: 29447
- Ever gold: 1127

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
