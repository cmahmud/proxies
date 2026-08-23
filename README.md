# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 115
- HTTP: 215 alive / 35 gold
- HTTPS: 83 alive / 3 gold
- SOCKS4: 98 alive / 0 gold
- SOCKS5: 251 alive / 77 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32672
- Ever gold: 1193

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
