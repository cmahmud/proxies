# SyndProxy private pool

## Current pool

- Alive now: 1019
- Gold now: 279
- HTTP: 410 alive / 29 gold
- HTTPS: 144 alive / 4 gold
- SOCKS4: 241 alive / 134 gold
- SOCKS5: 224 alive / 112 gold

## Historical pool

- Discovered: 100094
- Ever alive: 12613
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
