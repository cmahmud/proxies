# SyndProxy private pool

## Current pool

- Alive now: 1322
- Gold now: 565
- HTTP: 550 alive / 194 gold
- HTTPS: 343 alive / 98 gold
- SOCKS4: 225 alive / 143 gold
- SOCKS5: 204 alive / 130 gold

## Historical pool

- Discovered: 136255
- Ever alive: 22788
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
