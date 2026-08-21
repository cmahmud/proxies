# SyndProxy private pool

## Current pool

- Alive now: 1079
- Gold now: 447
- HTTP: 354 alive / 105 gold
- HTTPS: 249 alive / 35 gold
- SOCKS4: 198 alive / 147 gold
- SOCKS5: 278 alive / 160 gold

## Historical pool

- Discovered: 153731
- Ever alive: 28667
- Ever gold: 1111

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
