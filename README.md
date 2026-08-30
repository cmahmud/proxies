# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 418
- HTTP: 125 alive / 78 gold
- HTTPS: 78 alive / 29 gold
- SOCKS4: 160 alive / 151 gold
- SOCKS5: 189 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44044
- Ever gold: 1393

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
