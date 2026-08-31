# SyndProxy validated proxy pool

## Current pool

- Alive now: 650
- Gold now: 478
- HTTP: 150 alive / 98 gold
- HTTPS: 134 alive / 41 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 199 alive / 180 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45217
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
