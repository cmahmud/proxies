# SyndProxy private pool

## Current pool

- Alive now: 629
- Gold now: 385
- HTTP: 162 alive / 68 gold
- HTTPS: 94 alive / 16 gold
- SOCKS4: 179 alive / 146 gold
- SOCKS5: 194 alive / 155 gold

## Historical pool

- Discovered: 146602
- Ever alive: 25685
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
