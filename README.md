# SyndProxy private pool

## Current pool

- Alive now: 1129
- Gold now: 401
- HTTP: 359 alive / 77 gold
- HTTPS: 237 alive / 14 gold
- SOCKS4: 270 alive / 155 gold
- SOCKS5: 263 alive / 155 gold

## Historical pool

- Discovered: 131718
- Ever alive: 20686
- Ever gold: 873

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
