# SyndProxy private pool

## Current pool

- Alive now: 736
- Gold now: 411
- HTTP: 191 alive / 85 gold
- HTTPS: 133 alive / 27 gold
- SOCKS4: 198 alive / 140 gold
- SOCKS5: 214 alive / 159 gold

## Historical pool

- Discovered: 162441
- Ever alive: 31426
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
