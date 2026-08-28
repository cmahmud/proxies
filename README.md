# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 397
- HTTP: 101 alive / 68 gold
- HTTPS: 89 alive / 14 gold
- SOCKS4: 156 alive / 154 gold
- SOCKS5: 177 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43203
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
