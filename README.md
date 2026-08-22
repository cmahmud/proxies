# SyndProxy private pool

## Current pool

- Alive now: 905
- Gold now: 406
- HTTP: 274 alive / 86 gold
- HTTPS: 167 alive / 23 gold
- SOCKS4: 212 alive / 132 gold
- SOCKS5: 252 alive / 165 gold

## Historical pool

- Discovered: 166560
- Ever alive: 32404
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
