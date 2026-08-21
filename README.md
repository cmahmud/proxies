# SyndProxy private pool

## Current pool

- Alive now: 1034
- Gold now: 455
- HTTP: 338 alive / 100 gold
- HTTPS: 216 alive / 33 gold
- SOCKS4: 206 alive / 149 gold
- SOCKS5: 274 alive / 173 gold

## Historical pool

- Discovered: 153740
- Ever alive: 28698
- Ever gold: 1112

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
