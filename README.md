# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 397
- HTTP: 79 alive / 53 gold
- HTTPS: 55 alive / 18 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 183 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41607
- Ever gold: 1341

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
