# SyndProxy private pool

## Current pool

- Alive now: 908
- Gold now: 425
- HTTP: 291 alive / 106 gold
- HTTPS: 163 alive / 35 gold
- SOCKS4: 218 alive / 138 gold
- SOCKS5: 236 alive / 146 gold

## Historical pool

- Discovered: 160258
- Ever alive: 30708
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
