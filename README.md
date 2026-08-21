# SyndProxy private pool

## Current pool

- Alive now: 821
- Gold now: 406
- HTTP: 231 alive / 89 gold
- HTTPS: 149 alive / 23 gold
- SOCKS4: 203 alive / 144 gold
- SOCKS5: 238 alive / 150 gold

## Historical pool

- Discovered: 152160
- Ever alive: 27807
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
