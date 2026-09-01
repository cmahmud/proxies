# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 418
- HTTP: 80 alive / 62 gold
- HTTPS: 43 alive / 24 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 179 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47093
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
