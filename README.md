# SyndProxy private pool

## Current pool

- Alive now: 1092
- Gold now: 524
- HTTP: 376 alive / 161 gold
- HTTPS: 253 alive / 93 gold
- SOCKS4: 249 alive / 144 gold
- SOCKS5: 214 alive / 126 gold

## Historical pool

- Discovered: 123226
- Ever alive: 18921
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
