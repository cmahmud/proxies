# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 395
- HTTP: 94 alive / 63 gold
- HTTPS: 75 alive / 17 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 170 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37547
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
