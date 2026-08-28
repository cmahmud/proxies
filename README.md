# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 397
- HTTP: 104 alive / 69 gold
- HTTPS: 96 alive / 17 gold
- SOCKS4: 156 alive / 153 gold
- SOCKS5: 179 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43203
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
