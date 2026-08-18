# SyndProxy private pool

## Current pool

- Alive now: 642
- Gold now: 241
- HTTP: 168 alive / 27 gold
- HTTPS: 93 alive / 8 gold
- SOCKS4: 192 alive / 119 gold
- SOCKS5: 189 alive / 87 gold

## Historical pool

- Discovered: 86742
- Ever alive: 6883
- Ever gold: 334

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
