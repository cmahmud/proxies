# SyndProxy private pool

## Current pool

- Alive now: 1025
- Gold now: 416
- HTTP: 359 alive / 106 gold
- HTTPS: 217 alive / 29 gold
- SOCKS4: 211 alive / 133 gold
- SOCKS5: 238 alive / 148 gold

## Historical pool

- Discovered: 160027
- Ever alive: 30625
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
