# SyndProxy private pool

## Current pool

- Alive now: 870
- Gold now: 410
- HTTP: 269 alive / 88 gold
- HTTPS: 160 alive / 26 gold
- SOCKS4: 220 alive / 148 gold
- SOCKS5: 221 alive / 148 gold

## Historical pool

- Discovered: 166322
- Ever alive: 32386
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
