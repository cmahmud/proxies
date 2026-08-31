# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 420
- HTTP: 96 alive / 58 gold
- HTTPS: 73 alive / 33 gold
- SOCKS4: 188 alive / 161 gold
- SOCKS5: 195 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45493
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
