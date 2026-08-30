# SyndProxy validated proxy pool

## Current pool

- Alive now: 594
- Gold now: 422
- HTTP: 127 alive / 81 gold
- HTTPS: 76 alive / 31 gold
- SOCKS4: 156 alive / 151 gold
- SOCKS5: 235 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43936
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
