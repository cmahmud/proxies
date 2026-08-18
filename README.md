# SyndProxy private pool

## Current pool

- Alive now: 1056
- Gold now: 319
- HTTP: 354 alive / 42 gold
- HTTPS: 217 alive / 11 gold
- SOCKS4: 245 alive / 137 gold
- SOCKS5: 240 alive / 129 gold

## Historical pool

- Discovered: 107044
- Ever alive: 14405
- Ever gold: 444

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
