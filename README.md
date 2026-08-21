# SyndProxy private pool

## Current pool

- Alive now: 1038
- Gold now: 431
- HTTP: 325 alive / 110 gold
- HTTPS: 217 alive / 33 gold
- SOCKS4: 244 alive / 147 gold
- SOCKS5: 252 alive / 141 gold

## Historical pool

- Discovered: 160278
- Ever alive: 30782
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
