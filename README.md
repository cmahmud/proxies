# SyndProxy private pool

## Current pool

- Alive now: 1271
- Gold now: 406
- HTTP: 401 alive / 93 gold
- HTTPS: 314 alive / 11 gold
- SOCKS4: 263 alive / 143 gold
- SOCKS5: 293 alive / 159 gold

## Historical pool

- Discovered: 131826
- Ever alive: 21039
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
