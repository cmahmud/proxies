# SyndProxy private pool

## Current pool

- Alive now: 956
- Gold now: 396
- HTTP: 301 alive / 86 gold
- HTTPS: 184 alive / 23 gold
- SOCKS4: 227 alive / 142 gold
- SOCKS5: 244 alive / 145 gold

## Historical pool

- Discovered: 157419
- Ever alive: 29721
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
