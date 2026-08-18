# SyndProxy private pool

## Current pool

- Alive now: 989
- Gold now: 294
- HTTP: 295 alive / 26 gold
- HTTPS: 195 alive / 4 gold
- SOCKS4: 251 alive / 145 gold
- SOCKS5: 248 alive / 119 gold

## Historical pool

- Discovered: 102805
- Ever alive: 12744
- Ever gold: 399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
