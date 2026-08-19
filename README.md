# SyndProxy private pool

## Current pool

- Alive now: 1108
- Gold now: 417
- HTTP: 349 alive / 84 gold
- HTTPS: 241 alive / 16 gold
- SOCKS4: 226 alive / 158 gold
- SOCKS5: 292 alive / 159 gold

## Historical pool

- Discovered: 134522
- Ever alive: 21848
- Ever gold: 888

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
