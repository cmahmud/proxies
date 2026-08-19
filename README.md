# SyndProxy private pool

## Current pool

- Alive now: 1007
- Gold now: 512
- HTTP: 345 alive / 149 gold
- HTTPS: 235 alive / 89 gold
- SOCKS4: 220 alive / 144 gold
- SOCKS5: 207 alive / 130 gold

## Historical pool

- Discovered: 117160
- Ever alive: 17661
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
