# SyndProxy private pool

## Current pool

- Alive now: 1161
- Gold now: 605
- HTTP: 450 alive / 193 gold
- HTTPS: 265 alive / 112 gold
- SOCKS4: 222 alive / 145 gold
- SOCKS5: 224 alive / 155 gold

## Historical pool

- Discovered: 124852
- Ever alive: 19423
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
