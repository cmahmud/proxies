# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 429
- HTTP: 106 alive / 75 gold
- HTTPS: 53 alive / 27 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 192 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44457
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
