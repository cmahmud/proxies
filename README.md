# SyndProxy validated proxy pool

## Current pool

- Alive now: 660
- Gold now: 413
- HTTP: 133 alive / 73 gold
- HTTPS: 181 alive / 19 gold
- SOCKS4: 168 alive / 156 gold
- SOCKS5: 178 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40404
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
