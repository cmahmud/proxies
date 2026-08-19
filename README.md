# SyndProxy private pool

## Current pool

- Alive now: 1048
- Gold now: 421
- HTTP: 307 alive / 88 gold
- HTTPS: 225 alive / 16 gold
- SOCKS4: 223 alive / 159 gold
- SOCKS5: 293 alive / 158 gold

## Historical pool

- Discovered: 134522
- Ever alive: 21839
- Ever gold: 888

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
