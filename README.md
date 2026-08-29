# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 393
- HTTP: 84 alive / 61 gold
- HTTPS: 71 alive / 19 gold
- SOCKS4: 166 alive / 157 gold
- SOCKS5: 166 alive / 156 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43399
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
