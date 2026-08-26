# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 397
- HTTP: 101 alive / 59 gold
- HTTPS: 36 alive / 15 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 177 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38970
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
