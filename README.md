# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 437
- HTTP: 138 alive / 74 gold
- HTTPS: 130 alive / 26 gold
- SOCKS4: 186 alive / 163 gold
- SOCKS5: 191 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47615
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
