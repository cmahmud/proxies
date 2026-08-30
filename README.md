# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 427
- HTTP: 100 alive / 73 gold
- HTTPS: 52 alive / 25 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 186 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44442
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
