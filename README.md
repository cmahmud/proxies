# SyndProxy validated proxy pool

## Current pool

- Alive now: 381
- Gold now: 331
- HTTP: 44 alive / 32 gold
- HTTPS: 12 alive / 1 gold
- SOCKS4: 159 alive / 150 gold
- SOCKS5: 166 alive / 148 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43600
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
