# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 474
- HTTP: 142 alive / 95 gold
- HTTPS: 124 alive / 37 gold
- SOCKS4: 189 alive / 163 gold
- SOCKS5: 196 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46345
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
