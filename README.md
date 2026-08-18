# SyndProxy private pool

## Current pool

- Alive now: 1101
- Gold now: 290
- HTTP: 364 alive / 30 gold
- HTTPS: 246 alive / 4 gold
- SOCKS4: 244 alive / 140 gold
- SOCKS5: 247 alive / 116 gold

## Historical pool

- Discovered: 100167
- Ever alive: 12666
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
