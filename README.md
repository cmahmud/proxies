# SyndProxy private pool

## Current pool

- Alive now: 961
- Gold now: 386
- HTTP: 324 alive / 85 gold
- HTTPS: 196 alive / 26 gold
- SOCKS4: 208 alive / 133 gold
- SOCKS5: 233 alive / 142 gold

## Historical pool

- Discovered: 157419
- Ever alive: 29712
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
