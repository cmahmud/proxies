# SyndProxy private pool

## Current pool

- Alive now: 1044
- Gold now: 318
- HTTP: 357 alive / 41 gold
- HTTPS: 202 alive / 11 gold
- SOCKS4: 248 alive / 137 gold
- SOCKS5: 237 alive / 129 gold

## Historical pool

- Discovered: 107043
- Ever alive: 14386
- Ever gold: 441

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
