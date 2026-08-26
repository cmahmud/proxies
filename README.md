# SyndProxy validated proxy pool

## Current pool

- Alive now: 615
- Gold now: 401
- HTTP: 128 alive / 74 gold
- HTTPS: 146 alive / 18 gold
- SOCKS4: 158 alive / 151 gold
- SOCKS5: 183 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40204
- Ever gold: 1307

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
