# SyndProxy private pool

## Current pool

- Alive now: 1224
- Gold now: 394
- HTTP: 405 alive / 91 gold
- HTTPS: 296 alive / 21 gold
- SOCKS4: 220 alive / 130 gold
- SOCKS5: 303 alive / 152 gold

## Historical pool

- Discovered: 134557
- Ever alive: 22142
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
