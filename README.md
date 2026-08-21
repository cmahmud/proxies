# SyndProxy private pool

## Current pool

- Alive now: 1069
- Gold now: 409
- HTTP: 364 alive / 107 gold
- HTTPS: 258 alive / 27 gold
- SOCKS4: 242 alive / 150 gold
- SOCKS5: 205 alive / 125 gold

## Historical pool

- Discovered: 160027
- Ever alive: 30589
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
