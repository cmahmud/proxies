# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 431
- HTTP: 112 alive / 81 gold
- HTTPS: 141 alive / 22 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 204 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42407
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
