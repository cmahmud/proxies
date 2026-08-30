# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 474
- HTTP: 139 alive / 98 gold
- HTTPS: 118 alive / 38 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 201 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44886
- Ever gold: 1417

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
