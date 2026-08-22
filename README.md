# SyndProxy private pool

## Current pool

- Alive now: 1018
- Gold now: 414
- HTTP: 314 alive / 91 gold
- HTTPS: 239 alive / 28 gold
- SOCKS4: 219 alive / 143 gold
- SOCKS5: 246 alive / 152 gold

## Historical pool

- Discovered: 164245
- Ever alive: 32080
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
