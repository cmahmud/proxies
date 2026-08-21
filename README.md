# SyndProxy private pool

## Current pool

- Alive now: 1386
- Gold now: 454
- HTTP: 478 alive / 104 gold
- HTTPS: 390 alive / 33 gold
- SOCKS4: 229 alive / 150 gold
- SOCKS5: 289 alive / 167 gold

## Historical pool

- Discovered: 159265
- Ever alive: 30350
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
