# SyndProxy private pool

## Current pool

- Alive now: 1290
- Gold now: 425
- HTTP: 475 alive / 101 gold
- HTTPS: 297 alive / 25 gold
- SOCKS4: 206 alive / 141 gold
- SOCKS5: 312 alive / 158 gold

## Historical pool

- Discovered: 136246
- Ever alive: 22640
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
