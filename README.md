# SyndProxy private pool

## Current pool

- Alive now: 907
- Gold now: 446
- HTTP: 297 alive / 116 gold
- HTTPS: 205 alive / 86 gold
- SOCKS4: 207 alive / 127 gold
- SOCKS5: 198 alive / 117 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17494
- Ever gold: 664

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
