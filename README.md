# SyndProxy private pool

## Current pool

- Alive now: 930
- Gold now: 286
- HTTP: 301 alive / 26 gold
- HTTPS: 162 alive / 4 gold
- SOCKS4: 232 alive / 143 gold
- SOCKS5: 235 alive / 113 gold

## Historical pool

- Discovered: 99165
- Ever alive: 12336
- Ever gold: 396

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
