# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 397
- HTTP: 93 alive / 66 gold
- HTTPS: 67 alive / 15 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 166 alive / 157 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37272
- Ever gold: 1284

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
