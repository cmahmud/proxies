# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 433
- HTTP: 119 alive / 74 gold
- HTTPS: 63 alive / 28 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 196 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45537
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
