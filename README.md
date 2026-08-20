# SyndProxy private pool

## Current pool

- Alive now: 1747
- Gold now: 664
- HTTP: 665 alive / 225 gold
- HTTPS: 521 alive / 121 gold
- SOCKS4: 249 alive / 150 gold
- SOCKS5: 312 alive / 168 gold

## Historical pool

- Discovered: 142702
- Ever alive: 24360
- Ever gold: 983

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
