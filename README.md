# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 397
- HTTP: 111 alive / 60 gold
- HTTPS: 40 alive / 13 gold
- SOCKS4: 170 alive / 157 gold
- SOCKS5: 190 alive / 167 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33656
- Ever gold: 1246

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
