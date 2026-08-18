# SyndProxy private pool

## Current pool

- Alive now: 890
- Gold now: 212
- HTTP: 305 alive / 34 gold
- HTTPS: 170 alive / 10 gold
- SOCKS4: 214 alive / 97 gold
- SOCKS5: 201 alive / 71 gold

## Historical pool

- Discovered: 86648
- Ever alive: 5725
- Ever gold: 288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
