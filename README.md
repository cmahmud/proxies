# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 418
- HTTP: 90 alive / 58 gold
- HTTPS: 73 alive / 32 gold
- SOCKS4: 188 alive / 161 gold
- SOCKS5: 194 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45493
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
