# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 425
- HTTP: 80 alive / 66 gold
- HTTPS: 68 alive / 27 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 180 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47146
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
