# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 423
- HTTP: 89 alive / 66 gold
- HTTPS: 90 alive / 27 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 182 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47132
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
