# SyndProxy private pool

## Current pool

- Alive now: 1112
- Gold now: 570
- HTTP: 361 alive / 186 gold
- HTTPS: 277 alive / 97 gold
- SOCKS4: 233 alive / 136 gold
- SOCKS5: 241 alive / 151 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23251
- Ever gold: 916

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
