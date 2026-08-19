# SyndProxy private pool

## Current pool

- Alive now: 1264
- Gold now: 386
- HTTP: 418 alive / 92 gold
- HTTPS: 312 alive / 18 gold
- SOCKS4: 244 alive / 137 gold
- SOCKS5: 290 alive / 139 gold

## Historical pool

- Discovered: 133943
- Ever alive: 21614
- Ever gold: 886

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
