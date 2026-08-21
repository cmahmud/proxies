# SyndProxy private pool

## Current pool

- Alive now: 969
- Gold now: 396
- HTTP: 339 alive / 82 gold
- HTTPS: 177 alive / 23 gold
- SOCKS4: 199 alive / 129 gold
- SOCKS5: 254 alive / 162 gold

## Historical pool

- Discovered: 157419
- Ever alive: 29710
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
