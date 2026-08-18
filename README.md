# SyndProxy private pool

## Current pool

- Alive now: 1036
- Gold now: 239
- HTTP: 365 alive / 29 gold
- HTTPS: 175 alive / 8 gold
- SOCKS4: 277 alive / 117 gold
- SOCKS5: 219 alive / 85 gold

## Historical pool

- Discovered: 86712
- Ever alive: 6879
- Ever gold: 320

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
