# SyndProxy private pool

## Current pool

- Alive now: 1017
- Gold now: 426
- HTTP: 311 alive / 85 gold
- HTTPS: 213 alive / 28 gold
- SOCKS4: 223 alive / 155 gold
- SOCKS5: 270 alive / 158 gold

## Historical pool

- Discovered: 164942
- Ever alive: 32192
- Ever gold: 1173

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
