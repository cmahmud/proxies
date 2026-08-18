# SyndProxy private pool

## Current pool

- Alive now: 901
- Gold now: 261
- HTTP: 284 alive / 31 gold
- HTTPS: 176 alive / 4 gold
- SOCKS4: 238 alive / 129 gold
- SOCKS5: 203 alive / 97 gold

## Historical pool

- Discovered: 95396
- Ever alive: 10615
- Ever gold: 378

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
