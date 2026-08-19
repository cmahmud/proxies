# SyndProxy private pool

## Current pool

- Alive now: 1051
- Gold now: 363
- HTTP: 340 alive / 65 gold
- HTTPS: 216 alive / 15 gold
- SOCKS4: 258 alive / 156 gold
- SOCKS5: 237 alive / 127 gold

## Historical pool

- Discovered: 110866
- Ever alive: 16026
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
