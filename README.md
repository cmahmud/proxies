# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 426
- HTTP: 86 alive / 68 gold
- HTTPS: 62 alive / 27 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 196 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45478
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
