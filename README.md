# SyndProxy private pool

## Current pool

- Alive now: 883
- Gold now: 320
- HTTP: 297 alive / 56 gold
- HTTPS: 189 alive / 10 gold
- SOCKS4: 202 alive / 128 gold
- SOCKS5: 195 alive / 126 gold

## Historical pool

- Discovered: 129252
- Ever alive: 20138
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
