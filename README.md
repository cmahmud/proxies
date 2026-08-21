# SyndProxy private pool

## Current pool

- Alive now: 1151
- Gold now: 372
- HTTP: 408 alive / 101 gold
- HTTPS: 278 alive / 23 gold
- SOCKS4: 202 alive / 111 gold
- SOCKS5: 263 alive / 137 gold

## Historical pool

- Discovered: 152758
- Ever alive: 28324
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
