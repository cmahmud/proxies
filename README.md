# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 381
- HTTP: 120 alive / 58 gold
- HTTPS: 46 alive / 7 gold
- SOCKS4: 166 alive / 155 gold
- SOCKS5: 179 alive / 161 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33442
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
