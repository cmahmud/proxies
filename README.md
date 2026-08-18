# SyndProxy private pool

## Current pool

- Alive now: 931
- Gold now: 325
- HTTP: 280 alive / 34 gold
- HTTPS: 195 alive / 10 gold
- SOCKS4: 227 alive / 148 gold
- SOCKS5: 229 alive / 133 gold

## Historical pool

- Discovered: 106999
- Ever alive: 14205
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
