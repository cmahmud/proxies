# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 475
- HTTP: 131 alive / 95 gold
- HTTPS: 119 alive / 38 gold
- SOCKS4: 183 alive / 162 gold
- SOCKS5: 193 alive / 180 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46348
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
