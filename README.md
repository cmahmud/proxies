# SyndProxy private pool

## Current pool

- Alive now: 1034
- Gold now: 342
- HTTP: 322 alive / 68 gold
- HTTPS: 258 alive / 18 gold
- SOCKS4: 238 alive / 141 gold
- SOCKS5: 216 alive / 115 gold

## Historical pool

- Discovered: 110913
- Ever alive: 16091
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
