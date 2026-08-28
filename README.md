# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 397
- HTTP: 82 alive / 55 gold
- HTTPS: 53 alive / 19 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 188 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42793
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
