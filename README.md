# SyndProxy private pool

## Current pool

- Alive now: 1006
- Gold now: 381
- HTTP: 297 alive / 91 gold
- HTTPS: 252 alive / 28 gold
- SOCKS4: 210 alive / 129 gold
- SOCKS5: 247 alive / 133 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25055
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
