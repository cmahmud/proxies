# SyndProxy private pool

## Current pool

- Alive now: 1176
- Gold now: 405
- HTTP: 373 alive / 93 gold
- HTTPS: 244 alive / 17 gold
- SOCKS4: 224 alive / 147 gold
- SOCKS5: 335 alive / 148 gold

## Historical pool

- Discovered: 131842
- Ever alive: 21201
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
