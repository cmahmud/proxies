# SyndProxy validated proxy pool

## Current pool

- Alive now: 388
- Gold now: 352
- HTTP: 48 alive / 36 gold
- HTTPS: 13 alive / 2 gold
- SOCKS4: 159 alive / 157 gold
- SOCKS5: 168 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43594
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
