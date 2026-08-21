# SyndProxy private pool

## Current pool

- Alive now: 809
- Gold now: 405
- HTTP: 233 alive / 88 gold
- HTTPS: 113 alive / 17 gold
- SOCKS4: 218 alive / 150 gold
- SOCKS5: 245 alive / 150 gold

## Historical pool

- Discovered: 155698
- Ever alive: 29279
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
