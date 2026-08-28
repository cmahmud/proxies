# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 397
- HTTP: 79 alive / 57 gold
- HTTPS: 77 alive / 19 gold
- SOCKS4: 166 alive / 157 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42745
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
