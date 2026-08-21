# SyndProxy private pool

## Current pool

- Alive now: 1292
- Gold now: 441
- HTTP: 438 alive / 102 gold
- HTTPS: 317 alive / 27 gold
- SOCKS4: 249 alive / 151 gold
- SOCKS5: 288 alive / 161 gold

## Historical pool

- Discovered: 159282
- Ever alive: 30458
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
