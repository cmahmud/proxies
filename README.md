# SyndProxy private pool

## Current pool

- Alive now: 1050
- Gold now: 433
- HTTP: 341 alive / 98 gold
- HTTPS: 272 alive / 34 gold
- SOCKS4: 188 alive / 131 gold
- SOCKS5: 249 alive / 170 gold

## Historical pool

- Discovered: 161922
- Ever alive: 31169
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
