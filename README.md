# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 411
- HTTP: 81 alive / 57 gold
- HTTPS: 51 alive / 24 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 180 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47097
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
