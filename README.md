# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 394
- HTTP: 145 alive / 68 gold
- HTTPS: 124 alive / 22 gold
- SOCKS4: 168 alive / 148 gold
- SOCKS5: 195 alive / 156 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39578
- Ever gold: 1299

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
