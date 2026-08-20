# SyndProxy private pool

## Current pool

- Alive now: 1909
- Gold now: 662
- HTTP: 751 alive / 223 gold
- HTTPS: 589 alive / 123 gold
- SOCKS4: 253 alive / 150 gold
- SOCKS5: 316 alive / 166 gold

## Historical pool

- Discovered: 142702
- Ever alive: 24360
- Ever gold: 983

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
