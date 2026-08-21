# SyndProxy private pool

## Current pool

- Alive now: 1342
- Gold now: 444
- HTTP: 499 alive / 102 gold
- HTTPS: 333 alive / 29 gold
- SOCKS4: 239 alive / 151 gold
- SOCKS5: 271 alive / 162 gold

## Historical pool

- Discovered: 159282
- Ever alive: 30468
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
