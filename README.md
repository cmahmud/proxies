# SyndProxy private pool

## Current pool

- Alive now: 785
- Gold now: 387
- HTTP: 205 alive / 90 gold
- HTTPS: 169 alive / 28 gold
- SOCKS4: 204 alive / 139 gold
- SOCKS5: 207 alive / 130 gold

## Historical pool

- Discovered: 162766
- Ever alive: 31633
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
