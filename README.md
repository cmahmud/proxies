# SyndProxy private pool

## Current pool

- Alive now: 981
- Gold now: 404
- HTTP: 314 alive / 96 gold
- HTTPS: 221 alive / 33 gold
- SOCKS4: 210 alive / 145 gold
- SOCKS5: 236 alive / 130 gold

## Historical pool

- Discovered: 160997
- Ever alive: 30950
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
