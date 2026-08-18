# SyndProxy private pool

## Current pool

- Alive now: 1029
- Gold now: 286
- HTTP: 358 alive / 29 gold
- HTTPS: 178 alive / 6 gold
- SOCKS4: 248 alive / 128 gold
- SOCKS5: 245 alive / 123 gold

## Historical pool

- Discovered: 102839
- Ever alive: 13131
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
