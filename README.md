# SyndProxy private pool

## Current pool

- Alive now: 987
- Gold now: 523
- HTTP: 347 alive / 155 gold
- HTTPS: 241 alive / 91 gold
- SOCKS4: 201 alive / 144 gold
- SOCKS5: 198 alive / 133 gold

## Historical pool

- Discovered: 127362
- Ever alive: 19895
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
