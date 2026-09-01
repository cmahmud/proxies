# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 409
- HTTP: 78 alive / 62 gold
- HTTPS: 98 alive / 23 gold
- SOCKS4: 165 alive / 158 gold
- SOCKS5: 176 alive / 166 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47204
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
