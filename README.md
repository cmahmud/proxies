# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 413
- HTTP: 77 alive / 64 gold
- HTTPS: 100 alive / 22 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 179 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47184
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
