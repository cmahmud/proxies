# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 390
- HTTP: 97 alive / 62 gold
- HTTPS: 78 alive / 14 gold
- SOCKS4: 165 alive / 156 gold
- SOCKS5: 173 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43444
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
