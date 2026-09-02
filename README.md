# SyndProxy validated proxy pool

## Current pool

- Alive now: 615
- Gold now: 444
- HTTP: 124 alive / 77 gold
- HTTPS: 111 alive / 28 gold
- SOCKS4: 183 alive / 162 gold
- SOCKS5: 197 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47565
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
