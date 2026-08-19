# SyndProxy private pool

## Current pool

- Alive now: 1012
- Gold now: 485
- HTTP: 324 alive / 123 gold
- HTTPS: 235 alive / 73 gold
- SOCKS4: 214 alive / 143 gold
- SOCKS5: 239 alive / 146 gold

## Historical pool

- Discovered: 113910
- Ever alive: 16902
- Ever gold: 626

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
