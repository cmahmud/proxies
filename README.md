# SyndProxy validated proxy pool

## Current pool

- Alive now: 433
- Gold now: 351
- HTTP: 79 alive / 46 gold
- HTTPS: 41 alive / 12 gold
- SOCKS4: 157 alive / 149 gold
- SOCKS5: 156 alive / 144 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43641
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
