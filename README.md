# SyndProxy validated proxy pool

## Current pool

- Alive now: 423
- Gold now: 363
- HTTP: 53 alive / 38 gold
- HTTPS: 38 alive / 6 gold
- SOCKS4: 162 alive / 157 gold
- SOCKS5: 170 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43556
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
