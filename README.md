# SyndProxy private pool

## Current pool

- Alive now: 731
- Gold now: 404
- HTTP: 173 alive / 86 gold
- HTTPS: 126 alive / 20 gold
- SOCKS4: 218 alive / 144 gold
- SOCKS5: 214 alive / 154 gold

## Historical pool

- Discovered: 151687
- Ever alive: 27729
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
