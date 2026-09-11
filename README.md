# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 423
- HTTP: 107 alive / 72 gold
- HTTPS: 44 alive / 20 gold
- SOCKS4: 173 alive / 166 gold
- SOCKS5: 174 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49008
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
