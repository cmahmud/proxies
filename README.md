# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 397
- HTTP: 90 alive / 57 gold
- HTTPS: 78 alive / 19 gold
- SOCKS4: 167 alive / 157 gold
- SOCKS5: 185 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38516
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
