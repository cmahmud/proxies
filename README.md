# SyndProxy private pool

## Current pool

- Alive now: 863
- Gold now: 276
- HTTP: 262 alive / 33 gold
- HTTPS: 166 alive / 5 gold
- SOCKS4: 227 alive / 134 gold
- SOCKS5: 208 alive / 104 gold

## Historical pool

- Discovered: 99078
- Ever alive: 11452
- Ever gold: 383

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
