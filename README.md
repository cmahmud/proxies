# SyndProxy private pool

## Current pool

- Alive now: 1047
- Gold now: 398
- HTTP: 295 alive / 73 gold
- HTTPS: 231 alive / 12 gold
- SOCKS4: 251 alive / 153 gold
- SOCKS5: 270 alive / 160 gold

## Historical pool

- Discovered: 131115
- Ever alive: 20599
- Ever gold: 869

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
