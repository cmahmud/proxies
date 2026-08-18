# SyndProxy private pool

## Current pool

- Alive now: 929
- Gold now: 340
- HTTP: 256 alive / 48 gold
- HTTPS: 223 alive / 10 gold
- SOCKS4: 213 alive / 141 gold
- SOCKS5: 237 alive / 141 gold

## Historical pool

- Discovered: 107059
- Ever alive: 14523
- Ever gold: 465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
