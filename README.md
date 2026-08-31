# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 471
- HTTP: 156 alive / 96 gold
- HTTPS: 119 alive / 36 gold
- SOCKS4: 179 alive / 163 gold
- SOCKS5: 195 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45248
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
