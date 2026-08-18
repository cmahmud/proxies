# SyndProxy private pool

## Current pool

- Alive now: 756
- Gold now: 234
- HTTP: 194 alive / 27 gold
- HTTPS: 108 alive / 8 gold
- SOCKS4: 238 alive / 114 gold
- SOCKS5: 216 alive / 85 gold

## Historical pool

- Discovered: 86775
- Ever alive: 7594
- Ever gold: 338

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
