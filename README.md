# SyndProxy validated proxy pool

## Current pool

- Alive now: 637
- Gold now: 397
- HTTP: 131 alive / 71 gold
- HTTPS: 156 alive / 22 gold
- SOCKS4: 167 alive / 148 gold
- SOCKS5: 183 alive / 156 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40139
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
