# SyndProxy validated proxy pool

## Current pool

- Alive now: 615
- Gold now: 474
- HTTP: 135 alive / 93 gold
- HTTPS: 109 alive / 39 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 197 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46356
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
