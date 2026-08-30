# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 428
- HTTP: 110 alive / 74 gold
- HTTPS: 69 alive / 25 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 179 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44419
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
