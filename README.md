# SyndProxy validated proxy pool

## Current pool

- Alive now: 650
- Gold now: 483
- HTTP: 156 alive / 105 gold
- HTTPS: 126 alive / 40 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 198 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45241
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
