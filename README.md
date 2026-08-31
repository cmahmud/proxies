# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 438
- HTTP: 111 alive / 75 gold
- HTTPS: 64 alive / 28 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 207 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45554
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
