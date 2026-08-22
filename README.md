# SyndProxy private pool

## Current pool

- Alive now: 1014
- Gold now: 396
- HTTP: 318 alive / 88 gold
- HTTPS: 217 alive / 23 gold
- SOCKS4: 238 alive / 136 gold
- SOCKS5: 241 alive / 149 gold

## Historical pool

- Discovered: 164246
- Ever alive: 32088
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
