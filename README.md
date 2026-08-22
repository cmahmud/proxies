# SyndProxy private pool

## Current pool

- Alive now: 977
- Gold now: 400
- HTTP: 283 alive / 83 gold
- HTTPS: 240 alive / 24 gold
- SOCKS4: 204 alive / 145 gold
- SOCKS5: 250 alive / 148 gold

## Historical pool

- Discovered: 165842
- Ever alive: 32372
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
