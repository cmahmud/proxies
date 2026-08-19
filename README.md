# SyndProxy private pool

## Current pool

- Alive now: 1165
- Gold now: 402
- HTTP: 396 alive / 93 gold
- HTTPS: 265 alive / 14 gold
- SOCKS4: 230 alive / 147 gold
- SOCKS5: 274 alive / 148 gold

## Historical pool

- Discovered: 131842
- Ever alive: 21233
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
