# SyndProxy private pool

## Current pool

- Alive now: 1307
- Gold now: 439
- HTTP: 446 alive / 101 gold
- HTTPS: 324 alive / 28 gold
- SOCKS4: 250 alive / 150 gold
- SOCKS5: 287 alive / 160 gold

## Historical pool

- Discovered: 159282
- Ever alive: 30460
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
