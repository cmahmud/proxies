# SyndProxy private pool

## Current pool

- Alive now: 897
- Gold now: 423
- HTTP: 245 alive / 81 gold
- HTTPS: 178 alive / 22 gold
- SOCKS4: 226 alive / 151 gold
- SOCKS5: 248 alive / 169 gold

## Historical pool

- Discovered: 155791
- Ever alive: 29332
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
