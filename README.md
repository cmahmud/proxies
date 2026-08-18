# SyndProxy private pool

## Current pool

- Alive now: 939
- Gold now: 343
- HTTP: 273 alive / 47 gold
- HTTPS: 208 alive / 13 gold
- SOCKS4: 226 alive / 142 gold
- SOCKS5: 232 alive / 141 gold

## Historical pool

- Discovered: 107067
- Ever alive: 14684
- Ever gold: 468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
