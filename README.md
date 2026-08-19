# SyndProxy private pool

## Current pool

- Alive now: 1000
- Gold now: 381
- HTTP: 334 alive / 67 gold
- HTTPS: 189 alive / 16 gold
- SOCKS4: 224 alive / 145 gold
- SOCKS5: 253 alive / 153 gold

## Historical pool

- Discovered: 111011
- Ever alive: 16109
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
