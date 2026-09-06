# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 396
- HTTP: 105 alive / 76 gold
- HTTPS: 46 alive / 17 gold
- SOCKS4: 170 alive / 150 gold
- SOCKS5: 172 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48202
- Ever gold: 1523

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
