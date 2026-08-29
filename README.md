# SyndProxy validated proxy pool

## Current pool

- Alive now: 396
- Gold now: 301
- HTTP: 56 alive / 27 gold
- HTTPS: 13 alive / 2 gold
- SOCKS4: 160 alive / 138 gold
- SOCKS5: 167 alive / 134 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43592
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
