# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 416
- HTTP: 81 alive / 66 gold
- HTTPS: 98 alive / 24 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 186 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47175
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
