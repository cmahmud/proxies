# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 397
- HTTP: 94 alive / 64 gold
- HTTPS: 80 alive / 19 gold
- SOCKS4: 168 alive / 156 gold
- SOCKS5: 180 alive / 158 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37604
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
