# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 416
- HTTP: 75 alive / 61 gold
- HTTPS: 50 alive / 20 gold
- SOCKS4: 192 alive / 163 gold
- SOCKS5: 180 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47119
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
