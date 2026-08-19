# SyndProxy private pool

## Current pool

- Alive now: 1061
- Gold now: 544
- HTTP: 387 alive / 177 gold
- HTTPS: 267 alive / 115 gold
- SOCKS4: 208 alive / 117 gold
- SOCKS5: 199 alive / 135 gold

## Historical pool

- Discovered: 124841
- Ever alive: 19304
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
