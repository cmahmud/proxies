# SyndProxy private pool

## Current pool

- Alive now: 584
- Gold now: 217
- HTTP: 161 alive / 30 gold
- HTTPS: 74 alive / 8 gold
- SOCKS4: 151 alive / 97 gold
- SOCKS5: 198 alive / 82 gold

## Historical pool

- Discovered: 91718
- Ever alive: 8690
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
