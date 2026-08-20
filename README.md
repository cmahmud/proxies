# SyndProxy private pool

## Current pool

- Alive now: 769
- Gold now: 365
- HTTP: 185 alive / 68 gold
- HTTPS: 148 alive / 17 gold
- SOCKS4: 190 alive / 121 gold
- SOCKS5: 246 alive / 159 gold

## Historical pool

- Discovered: 148333
- Ever alive: 26097
- Ever gold: 1078

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
