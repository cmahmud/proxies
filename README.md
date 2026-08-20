# SyndProxy private pool

## Current pool

- Alive now: 895
- Gold now: 412
- HTTP: 226 alive / 90 gold
- HTTPS: 253 alive / 19 gold
- SOCKS4: 201 alive / 152 gold
- SOCKS5: 215 alive / 151 gold

## Historical pool

- Discovered: 151674
- Ever alive: 27555
- Ever gold: 1099

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
