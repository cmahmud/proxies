# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 464
- HTTP: 145 alive / 94 gold
- HTTPS: 112 alive / 33 gold
- SOCKS4: 189 alive / 162 gold
- SOCKS5: 201 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46308
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
