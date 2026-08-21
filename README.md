# SyndProxy private pool

## Current pool

- Alive now: 821
- Gold now: 424
- HTTP: 195 alive / 80 gold
- HTTPS: 156 alive / 24 gold
- SOCKS4: 224 alive / 148 gold
- SOCKS5: 246 alive / 172 gold

## Historical pool

- Discovered: 155791
- Ever alive: 29332
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
