# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 428
- HTTP: 118 alive / 81 gold
- HTTPS: 128 alive / 20 gold
- SOCKS4: 182 alive / 159 gold
- SOCKS5: 196 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42383
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
