# SyndProxy private pool

## Current pool

- Alive now: 796
- Gold now: 303
- HTTP: 222 alive / 57 gold
- HTTPS: 161 alive / 11 gold
- SOCKS4: 217 alive / 115 gold
- SOCKS5: 196 alive / 120 gold

## Historical pool

- Discovered: 129265
- Ever alive: 20147
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
