# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 438
- HTTP: 111 alive / 79 gold
- HTTPS: 76 alive / 29 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 202 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45463
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
