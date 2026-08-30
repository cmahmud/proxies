# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 431
- HTTP: 98 alive / 74 gold
- HTTPS: 53 alive / 27 gold
- SOCKS4: 165 alive / 161 gold
- SOCKS5: 190 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44440
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
