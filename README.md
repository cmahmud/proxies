# SyndProxy private pool

## Current pool

- Alive now: 1065
- Gold now: 318
- HTTP: 357 alive / 41 gold
- HTTPS: 218 alive / 11 gold
- SOCKS4: 254 alive / 137 gold
- SOCKS5: 236 alive / 129 gold

## Historical pool

- Discovered: 107043
- Ever alive: 14390
- Ever gold: 441

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
