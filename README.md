# SyndProxy private pool

## Current pool

- Alive now: 817
- Gold now: 225
- HTTP: 269 alive / 35 gold
- HTTPS: 120 alive / 9 gold
- SOCKS4: 218 alive / 112 gold
- SOCKS5: 210 alive / 69 gold

## Historical pool

- Discovered: 94324
- Ever alive: 9328
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
