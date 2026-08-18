# SyndProxy private pool

## Current pool

- Alive now: 991
- Gold now: 239
- HTTP: 413 alive / 31 gold
- HTTPS: 147 alive / 7 gold
- SOCKS4: 213 alive / 109 gold
- SOCKS5: 218 alive / 92 gold

## Historical pool

- Discovered: 91718
- Ever alive: 9052
- Ever gold: 361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
