# SyndProxy private pool

## Current pool

- Alive now: 944
- Gold now: 380
- HTTP: 304 alive / 86 gold
- HTTPS: 190 alive / 22 gold
- SOCKS4: 198 alive / 115 gold
- SOCKS5: 252 alive / 157 gold

## Historical pool

- Discovered: 166337
- Ever alive: 32399
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
