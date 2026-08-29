# SyndProxy validated proxy pool

## Current pool

- Alive now: 430
- Gold now: 347
- HTTP: 78 alive / 44 gold
- HTTPS: 39 alive / 11 gold
- SOCKS4: 156 alive / 147 gold
- SOCKS5: 157 alive / 145 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43640
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
