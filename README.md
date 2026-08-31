# SyndProxy validated proxy pool

## Current pool

- Alive now: 691
- Gold now: 477
- HTTP: 155 alive / 99 gold
- HTTPS: 138 alive / 37 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 228 alive / 180 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45260
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
