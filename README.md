# SyndProxy private pool

## Current pool

- Alive now: 777
- Gold now: 414
- HTTP: 206 alive / 88 gold
- HTTPS: 162 alive / 22 gold
- SOCKS4: 201 alive / 148 gold
- SOCKS5: 208 alive / 156 gold

## Historical pool

- Discovered: 151067
- Ever alive: 27412
- Ever gold: 1096

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
