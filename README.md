# SyndProxy private pool

## Current pool

- Alive now: 744
- Gold now: 388
- HTTP: 191 alive / 78 gold
- HTTPS: 142 alive / 21 gold
- SOCKS4: 208 alive / 146 gold
- SOCKS5: 203 alive / 143 gold

## Historical pool

- Discovered: 149497
- Ever alive: 26629
- Ever gold: 1086

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
