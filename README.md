# SyndProxy private pool

## Current pool

- Alive now: 1248
- Gold now: 513
- HTTP: 453 alive / 181 gold
- HTTPS: 351 alive / 51 gold
- SOCKS4: 207 alive / 121 gold
- SOCKS5: 237 alive / 160 gold

## Historical pool

- Discovered: 125667
- Ever alive: 19632
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
