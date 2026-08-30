# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 421
- HTTP: 107 alive / 70 gold
- HTTPS: 67 alive / 22 gold
- SOCKS4: 162 alive / 162 gold
- SOCKS5: 180 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44380
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
