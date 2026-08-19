# SyndProxy private pool

## Current pool

- Alive now: 1156
- Gold now: 404
- HTTP: 363 alive / 77 gold
- HTTPS: 250 alive / 13 gold
- SOCKS4: 273 alive / 156 gold
- SOCKS5: 270 alive / 158 gold

## Historical pool

- Discovered: 131718
- Ever alive: 20682
- Ever gold: 873

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
