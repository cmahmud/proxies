# SyndProxy private pool

## Current pool

- Alive now: 1088
- Gold now: 395
- HTTP: 376 alive / 113 gold
- HTTPS: 251 alive / 28 gold
- SOCKS4: 214 alive / 112 gold
- SOCKS5: 247 alive / 142 gold

## Historical pool

- Discovered: 160253
- Ever alive: 30682
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
