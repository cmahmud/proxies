# SyndProxy private pool

## Current pool

- Alive now: 1126
- Gold now: 440
- HTTP: 398 alive / 108 gold
- HTTPS: 255 alive / 29 gold
- SOCKS4: 224 alive / 134 gold
- SOCKS5: 249 alive / 169 gold

## Historical pool

- Discovered: 160214
- Ever alive: 30662
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
