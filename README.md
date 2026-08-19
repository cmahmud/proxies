# SyndProxy private pool

## Current pool

- Alive now: 952
- Gold now: 334
- HTTP: 283 alive / 58 gold
- HTTPS: 224 alive / 12 gold
- SOCKS4: 227 alive / 139 gold
- SOCKS5: 218 alive / 125 gold

## Historical pool

- Discovered: 129286
- Ever alive: 20266
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
