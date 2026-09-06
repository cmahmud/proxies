# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 408
- HTTP: 118 alive / 81 gold
- HTTPS: 69 alive / 18 gold
- SOCKS4: 167 alive / 152 gold
- SOCKS5: 180 alive / 157 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48066
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
