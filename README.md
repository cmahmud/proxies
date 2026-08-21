# SyndProxy private pool

## Current pool

- Alive now: 1152
- Gold now: 405
- HTTP: 424 alive / 109 gold
- HTTPS: 278 alive / 23 gold
- SOCKS4: 225 alive / 150 gold
- SOCKS5: 225 alive / 123 gold

## Historical pool

- Discovered: 153722
- Ever alive: 28550
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
