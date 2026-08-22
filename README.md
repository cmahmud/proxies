# SyndProxy private pool

## Current pool

- Alive now: 1029
- Gold now: 436
- HTTP: 338 alive / 98 gold
- HTTPS: 253 alive / 36 gold
- SOCKS4: 180 alive / 131 gold
- SOCKS5: 258 alive / 171 gold

## Historical pool

- Discovered: 161922
- Ever alive: 31168
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
