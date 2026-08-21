# SyndProxy private pool

## Current pool

- Alive now: 741
- Gold now: 400
- HTTP: 191 alive / 86 gold
- HTTPS: 131 alive / 19 gold
- SOCKS4: 215 alive / 143 gold
- SOCKS5: 204 alive / 152 gold

## Historical pool

- Discovered: 151687
- Ever alive: 27737
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
