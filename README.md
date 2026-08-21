# SyndProxy private pool

## Current pool

- Alive now: 962
- Gold now: 424
- HTTP: 300 alive / 90 gold
- HTTPS: 218 alive / 21 gold
- SOCKS4: 198 alive / 148 gold
- SOCKS5: 246 alive / 165 gold

## Historical pool

- Discovered: 153747
- Ever alive: 28770
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
