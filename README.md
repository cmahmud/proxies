# SyndProxy private pool

## Current pool

- Alive now: 1175
- Gold now: 394
- HTTP: 387 alive / 87 gold
- HTTPS: 298 alive / 15 gold
- SOCKS4: 231 alive / 129 gold
- SOCKS5: 259 alive / 163 gold

## Historical pool

- Discovered: 131856
- Ever alive: 21331
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
