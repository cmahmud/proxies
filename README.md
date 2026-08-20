# SyndProxy private pool

## Current pool

- Alive now: 870
- Gold now: 405
- HTTP: 236 alive / 75 gold
- HTTPS: 167 alive / 22 gold
- SOCKS4: 237 alive / 151 gold
- SOCKS5: 230 alive / 157 gold

## Historical pool

- Discovered: 151066
- Ever alive: 27386
- Ever gold: 1096

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
