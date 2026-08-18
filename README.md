# SyndProxy private pool

## Current pool

- Alive now: 965
- Gold now: 319
- HTTP: 290 alive / 38 gold
- HTTPS: 197 alive / 10 gold
- SOCKS4: 239 alive / 138 gold
- SOCKS5: 239 alive / 133 gold

## Historical pool

- Discovered: 107013
- Ever alive: 14242
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
