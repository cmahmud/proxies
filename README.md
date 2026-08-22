# SyndProxy private pool

## Current pool

- Alive now: 1030
- Gold now: 386
- HTTP: 302 alive / 86 gold
- HTTPS: 250 alive / 29 gold
- SOCKS4: 221 alive / 122 gold
- SOCKS5: 257 alive / 149 gold

## Historical pool

- Discovered: 164184
- Ever alive: 32057
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
