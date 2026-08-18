# SyndProxy private pool

## Current pool

- Alive now: 959
- Gold now: 243
- HTTP: 418 alive / 33 gold
- HTTPS: 151 alive / 6 gold
- SOCKS4: 233 alive / 139 gold
- SOCKS5: 157 alive / 65 gold

## Historical pool

- Discovered: 102867
- Ever alive: 13642
- Ever gold: 426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
