# SyndProxy private pool

## Current pool

- Alive now: 1083
- Gold now: 514
- HTTP: 385 alive / 148 gold
- HTTPS: 261 alive / 90 gold
- SOCKS4: 224 alive / 144 gold
- SOCKS5: 213 alive / 132 gold

## Historical pool

- Discovered: 117170
- Ever alive: 17674
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
