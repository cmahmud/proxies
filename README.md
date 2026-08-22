# SyndProxy private pool

## Current pool

- Alive now: 1029
- Gold now: 432
- HTTP: 333 alive / 96 gold
- HTTPS: 231 alive / 36 gold
- SOCKS4: 188 alive / 127 gold
- SOCKS5: 277 alive / 173 gold

## Historical pool

- Discovered: 161922
- Ever alive: 31154
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
