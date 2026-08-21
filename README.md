# SyndProxy private pool

## Current pool

- Alive now: 780
- Gold now: 400
- HTTP: 227 alive / 90 gold
- HTTPS: 145 alive / 23 gold
- SOCKS4: 188 alive / 128 gold
- SOCKS5: 220 alive / 159 gold

## Historical pool

- Discovered: 151681
- Ever alive: 27687
- Ever gold: 1102

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
