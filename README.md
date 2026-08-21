# SyndProxy private pool

## Current pool

- Alive now: 1267
- Gold now: 439
- HTTP: 432 alive / 97 gold
- HTTPS: 305 alive / 31 gold
- SOCKS4: 251 alive / 151 gold
- SOCKS5: 279 alive / 160 gold

## Historical pool

- Discovered: 159282
- Ever alive: 30451
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
