# SyndProxy private pool

## Current pool

- Alive now: 681
- Gold now: 201
- HTTP: 148 alive / 22 gold
- HTTPS: 122 alive / 9 gold
- SOCKS4: 204 alive / 90 gold
- SOCKS5: 207 alive / 80 gold

## Historical pool

- Discovered: 89623
- Ever alive: 7998
- Ever gold: 343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
