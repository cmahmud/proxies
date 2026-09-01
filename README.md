# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 420
- HTTP: 80 alive / 63 gold
- HTTPS: 74 alive / 25 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 178 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47125
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
