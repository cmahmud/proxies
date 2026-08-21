# SyndProxy private pool

## Current pool

- Alive now: 970
- Gold now: 403
- HTTP: 307 alive / 96 gold
- HTTPS: 214 alive / 21 gold
- SOCKS4: 198 alive / 135 gold
- SOCKS5: 251 alive / 151 gold

## Historical pool

- Discovered: 152167
- Ever alive: 27905
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
