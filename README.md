# SyndProxy validated proxy pool

## Current pool

- Alive now: 676
- Gold now: 476
- HTTP: 162 alive / 100 gold
- HTTPS: 119 alive / 37 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 215 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45255
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
