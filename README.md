# SyndProxy private pool

## Current pool

- Alive now: 1277
- Gold now: 411
- HTTP: 445 alive / 98 gold
- HTTPS: 285 alive / 17 gold
- SOCKS4: 241 alive / 141 gold
- SOCKS5: 306 alive / 155 gold

## Historical pool

- Discovered: 131826
- Ever alive: 20972
- Ever gold: 877

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
