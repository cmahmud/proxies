# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 397
- HTTP: 90 alive / 62 gold
- HTTPS: 76 alive / 19 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 174 alive / 158 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37558
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
