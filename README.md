# SyndProxy private pool

## Current pool

- Alive now: 1015
- Gold now: 362
- HTTP: 354 alive / 72 gold
- HTTPS: 204 alive / 15 gold
- SOCKS4: 240 alive / 150 gold
- SOCKS5: 217 alive / 125 gold

## Historical pool

- Discovered: 110913
- Ever alive: 16044
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
