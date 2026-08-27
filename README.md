# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 413
- HTTP: 93 alive / 71 gold
- HTTPS: 119 alive / 20 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41989
- Ever gold: 1347

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
