# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 475
- HTTP: 134 alive / 95 gold
- HTTPS: 121 alive / 38 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 193 alive / 180 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46350
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
