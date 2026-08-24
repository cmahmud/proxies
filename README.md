# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 390
- HTTP: 113 alive / 61 gold
- HTTPS: 49 alive / 13 gold
- SOCKS4: 165 alive / 156 gold
- SOCKS5: 184 alive / 160 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33440
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
