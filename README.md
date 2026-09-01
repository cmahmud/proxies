# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 448
- HTTP: 102 alive / 79 gold
- HTTPS: 100 alive / 30 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 189 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47387
- Ever gold: 1467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
