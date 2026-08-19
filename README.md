# SyndProxy private pool

## Current pool

- Alive now: 958
- Gold now: 335
- HTTP: 276 alive / 59 gold
- HTTPS: 220 alive / 13 gold
- SOCKS4: 244 alive / 140 gold
- SOCKS5: 218 alive / 123 gold

## Historical pool

- Discovered: 129286
- Ever alive: 20266
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
