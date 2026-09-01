# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 452
- HTTP: 125 alive / 86 gold
- HTTPS: 132 alive / 31 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 193 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46615
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
