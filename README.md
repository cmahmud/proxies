# SyndProxy private pool

## Current pool

- Alive now: 1074
- Gold now: 426
- HTTP: 352 alive / 86 gold
- HTTPS: 201 alive / 25 gold
- SOCKS4: 251 alive / 150 gold
- SOCKS5: 270 alive / 165 gold

## Historical pool

- Discovered: 163873
- Ever alive: 32010
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
