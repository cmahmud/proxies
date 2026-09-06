# SyndProxy validated proxy pool

## Current pool

- Alive now: 464
- Gold now: 371
- HTTP: 85 alive / 56 gold
- HTTPS: 35 alive / 9 gold
- SOCKS4: 168 alive / 153 gold
- SOCKS5: 176 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48292
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
