# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 413
- HTTP: 76 alive / 64 gold
- HTTPS: 99 alive / 22 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 180 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47182
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
