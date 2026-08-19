# SyndProxy private pool

## Current pool

- Alive now: 1045
- Gold now: 522
- HTTP: 364 alive / 151 gold
- HTTPS: 251 alive / 88 gold
- SOCKS4: 224 alive / 148 gold
- SOCKS5: 206 alive / 135 gold

## Historical pool

- Discovered: 117170
- Ever alive: 17708
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
