# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 411
- HTTP: 86 alive / 63 gold
- HTTPS: 90 alive / 24 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 180 alive / 166 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47226
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
