# SyndProxy private pool

## Current pool

- Alive now: 1208
- Gold now: 394
- HTTP: 427 alive / 100 gold
- HTTPS: 316 alive / 26 gold
- SOCKS4: 208 alive / 123 gold
- SOCKS5: 257 alive / 145 gold

## Historical pool

- Discovered: 152746
- Ever alive: 28097
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
