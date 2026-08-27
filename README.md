# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 413
- HTTP: 103 alive / 71 gold
- HTTPS: 103 alive / 22 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 177 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41803
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
