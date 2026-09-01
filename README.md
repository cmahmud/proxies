# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 421
- HTTP: 88 alive / 61 gold
- HTTPS: 39 alive / 27 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 179 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47092
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
