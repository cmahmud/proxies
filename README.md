# SyndProxy private pool

## Current pool

- Alive now: 1343
- Gold now: 439
- HTTP: 465 alive / 102 gold
- HTTPS: 359 alive / 27 gold
- SOCKS4: 246 alive / 150 gold
- SOCKS5: 273 alive / 160 gold

## Historical pool

- Discovered: 159282
- Ever alive: 30467
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
