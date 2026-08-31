# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 419
- HTTP: 108 alive / 66 gold
- HTTPS: 71 alive / 21 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 198 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45519
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
