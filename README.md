# SyndProxy private pool

## Current pool

- Alive now: 1077
- Gold now: 523
- HTTP: 371 alive / 154 gold
- HTTPS: 281 alive / 87 gold
- SOCKS4: 222 alive / 147 gold
- SOCKS5: 203 alive / 135 gold

## Historical pool

- Discovered: 117177
- Ever alive: 17734
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
