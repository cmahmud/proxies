# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 388
- HTTP: 114 alive / 66 gold
- HTTPS: 104 alive / 18 gold
- SOCKS4: 169 alive / 150 gold
- SOCKS5: 180 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39312
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
