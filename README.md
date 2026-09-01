# SyndProxy validated proxy pool

## Current pool

- Alive now: 615
- Gold now: 456
- HTTP: 129 alive / 84 gold
- HTTPS: 128 alive / 33 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 189 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46790
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
