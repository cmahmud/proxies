# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 413
- HTTP: 132 alive / 72 gold
- HTTPS: 170 alive / 23 gold
- SOCKS4: 169 alive / 156 gold
- SOCKS5: 180 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40436
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
