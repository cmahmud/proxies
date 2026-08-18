# SyndProxy private pool

## Current pool

- Alive now: 851
- Gold now: 256
- HTTP: 258 alive / 28 gold
- HTTPS: 170 alive / 4 gold
- SOCKS4: 204 alive / 116 gold
- SOCKS5: 219 alive / 108 gold

## Historical pool

- Discovered: 99106
- Ever alive: 11821
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
