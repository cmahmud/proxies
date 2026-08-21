# SyndProxy private pool

## Current pool

- Alive now: 1039
- Gold now: 380
- HTTP: 322 alive / 103 gold
- HTTPS: 236 alive / 32 gold
- SOCKS4: 217 alive / 110 gold
- SOCKS5: 264 alive / 135 gold

## Historical pool

- Discovered: 152758
- Ever alive: 28313
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
