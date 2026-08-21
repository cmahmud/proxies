# SyndProxy private pool

## Current pool

- Alive now: 1313
- Gold now: 439
- HTTP: 454 alive / 100 gold
- HTTPS: 328 alive / 27 gold
- SOCKS4: 250 alive / 151 gold
- SOCKS5: 281 alive / 161 gold

## Historical pool

- Discovered: 159282
- Ever alive: 30461
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
