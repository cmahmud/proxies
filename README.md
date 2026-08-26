# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 397
- HTTP: 86 alive / 56 gold
- HTTPS: 59 alive / 15 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 181 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39062
- Ever gold: 1296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
