# SyndProxy private pool

## Current pool

- Alive now: 1032
- Gold now: 518
- HTTP: 361 alive / 149 gold
- HTTPS: 247 alive / 92 gold
- SOCKS4: 218 alive / 148 gold
- SOCKS5: 206 alive / 129 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17615
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
