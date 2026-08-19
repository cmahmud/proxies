# SyndProxy private pool

## Current pool

- Alive now: 1129
- Gold now: 525
- HTTP: 415 alive / 153 gold
- HTTPS: 283 alive / 89 gold
- SOCKS4: 224 alive / 148 gold
- SOCKS5: 207 alive / 135 gold

## Historical pool

- Discovered: 117177
- Ever alive: 17734
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
