# SyndProxy private pool

## Current pool

- Alive now: 645
- Gold now: 252
- HTTP: 162 alive / 35 gold
- HTTPS: 82 alive / 7 gold
- SOCKS4: 206 alive / 126 gold
- SOCKS5: 195 alive / 84 gold

## Historical pool

- Discovered: 94326
- Ever alive: 9351
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
