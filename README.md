# SyndProxy private pool

## Current pool

- Alive now: 968
- Gold now: 308
- HTTP: 300 alive / 37 gold
- HTTPS: 212 alive / 9 gold
- SOCKS4: 233 alive / 137 gold
- SOCKS5: 223 alive / 125 gold

## Historical pool

- Discovered: 106999
- Ever alive: 14205
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
