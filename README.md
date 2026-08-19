# SyndProxy private pool

## Current pool

- Alive now: 1024
- Gold now: 351
- HTTP: 316 alive / 68 gold
- HTTPS: 245 alive / 11 gold
- SOCKS4: 234 alive / 125 gold
- SOCKS5: 229 alive / 147 gold

## Historical pool

- Discovered: 129286
- Ever alive: 20272
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
