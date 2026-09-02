# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 452
- HTTP: 100 alive / 78 gold
- HTTPS: 106 alive / 33 gold
- SOCKS4: 179 alive / 165 gold
- SOCKS5: 190 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47427
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
