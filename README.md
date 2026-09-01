# SyndProxy validated proxy pool

## Current pool

- Alive now: 583
- Gold now: 448
- HTTP: 106 alive / 78 gold
- HTTPS: 113 alive / 30 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 188 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47367
- Ever gold: 1467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
