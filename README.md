# SyndProxy private pool

## Current pool

- Alive now: 1034
- Gold now: 363
- HTTP: 332 alive / 82 gold
- HTTPS: 241 alive / 19 gold
- SOCKS4: 202 alive / 127 gold
- SOCKS5: 259 alive / 135 gold

## Historical pool

- Discovered: 158223
- Ever alive: 29846
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
