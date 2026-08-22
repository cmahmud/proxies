# SyndProxy private pool

## Current pool

- Alive now: 1040
- Gold now: 407
- HTTP: 320 alive / 93 gold
- HTTPS: 234 alive / 29 gold
- SOCKS4: 246 alive / 149 gold
- SOCKS5: 240 alive / 136 gold

## Historical pool

- Discovered: 161993
- Ever alive: 31317
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
