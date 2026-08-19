# SyndProxy private pool

## Current pool

- Alive now: 1179
- Gold now: 457
- HTTP: 445 alive / 117 gold
- HTTPS: 296 alive / 72 gold
- SOCKS4: 224 alive / 140 gold
- SOCKS5: 214 alive / 128 gold

## Historical pool

- Discovered: 113568
- Ever alive: 16749
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
