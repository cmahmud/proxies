# SyndProxy private pool

## Current pool

- Alive now: 1179
- Gold now: 406
- HTTP: 387 alive / 94 gold
- HTTPS: 257 alive / 14 gold
- SOCKS4: 233 alive / 150 gold
- SOCKS5: 302 alive / 148 gold

## Historical pool

- Discovered: 131840
- Ever alive: 21163
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
