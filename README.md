# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 447
- HTTP: 115 alive / 80 gold
- HTTPS: 129 alive / 39 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 188 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44735
- Ever gold: 1412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
