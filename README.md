# SyndProxy validated proxy pool

## Current pool

- Alive now: 615
- Gold now: 419
- HTTP: 103 alive / 69 gold
- HTTPS: 151 alive / 23 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 187 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41298
- Ever gold: 1323

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
