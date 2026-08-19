# SyndProxy private pool

## Current pool

- Alive now: 1128
- Gold now: 416
- HTTP: 369 alive / 86 gold
- HTTPS: 258 alive / 15 gold
- SOCKS4: 246 alive / 155 gold
- SOCKS5: 255 alive / 160 gold

## Historical pool

- Discovered: 131722
- Ever alive: 20765
- Ever gold: 875

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
