# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 427
- HTTP: 100 alive / 74 gold
- HTTPS: 55 alive / 25 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 193 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44461
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
