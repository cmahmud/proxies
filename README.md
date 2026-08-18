# SyndProxy private pool

## Current pool

- Alive now: 666
- Gold now: 251
- HTTP: 153 alive / 36 gold
- HTTPS: 97 alive / 8 gold
- SOCKS4: 216 alive / 126 gold
- SOCKS5: 200 alive / 81 gold

## Historical pool

- Discovered: 94326
- Ever alive: 9351
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
