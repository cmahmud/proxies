# SyndProxy validated proxy pool

## Current pool

- Alive now: 432
- Gold now: 364
- HTTP: 55 alive / 46 gold
- HTTPS: 45 alive / 7 gold
- SOCKS4: 162 alive / 156 gold
- SOCKS5: 170 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43543
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
