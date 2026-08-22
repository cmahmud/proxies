# SyndProxy private pool

## Current pool

- Alive now: 1015
- Gold now: 385
- HTTP: 284 alive / 86 gold
- HTTPS: 256 alive / 28 gold
- SOCKS4: 219 alive / 122 gold
- SOCKS5: 256 alive / 149 gold

## Historical pool

- Discovered: 164184
- Ever alive: 32054
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
