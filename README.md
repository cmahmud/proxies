# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 397
- HTTP: 92 alive / 63 gold
- HTTPS: 91 alive / 19 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 170 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37255
- Ever gold: 1284

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
