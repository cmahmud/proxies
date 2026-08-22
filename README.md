# SyndProxy private pool

## Current pool

- Alive now: 912
- Gold now: 406
- HTTP: 260 alive / 89 gold
- HTTPS: 183 alive / 29 gold
- SOCKS4: 233 alive / 150 gold
- SOCKS5: 236 alive / 138 gold

## Historical pool

- Discovered: 161993
- Ever alive: 31323
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
