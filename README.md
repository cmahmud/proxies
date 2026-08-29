# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 413
- HTTP: 112 alive / 74 gold
- HTTPS: 61 alive / 28 gold
- SOCKS4: 156 alive / 153 gold
- SOCKS5: 170 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43655
- Ever gold: 1376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
