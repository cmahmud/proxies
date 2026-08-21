# SyndProxy private pool

## Current pool

- Alive now: 1111
- Gold now: 419
- HTTP: 371 alive / 93 gold
- HTTPS: 252 alive / 24 gold
- SOCKS4: 227 alive / 147 gold
- SOCKS5: 261 alive / 155 gold

## Historical pool

- Discovered: 156426
- Ever alive: 29513
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
