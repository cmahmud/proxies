# SyndProxy private pool

## Current pool

- Alive now: 1216
- Gold now: 412
- HTTP: 381 alive / 91 gold
- HTTPS: 294 alive / 20 gold
- SOCKS4: 236 alive / 141 gold
- SOCKS5: 305 alive / 160 gold

## Historical pool

- Discovered: 136182
- Ever alive: 22224
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
