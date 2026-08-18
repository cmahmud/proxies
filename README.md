# SyndProxy private pool

## Current pool

- Alive now: 918
- Gold now: 260
- HTTP: 302 alive / 30 gold
- HTTPS: 174 alive / 4 gold
- SOCKS4: 239 alive / 129 gold
- SOCKS5: 203 alive / 97 gold

## Historical pool

- Discovered: 95395
- Ever alive: 10615
- Ever gold: 378

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
