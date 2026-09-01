# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 413
- HTTP: 81 alive / 63 gold
- HTTPS: 102 alive / 26 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 180 alive / 166 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47223
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
