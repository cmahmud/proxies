# SyndProxy private pool

## Current pool

- Alive now: 1039
- Gold now: 387
- HTTP: 336 alive / 88 gold
- HTTPS: 226 alive / 30 gold
- SOCKS4: 238 alive / 142 gold
- SOCKS5: 239 alive / 127 gold

## Historical pool

- Discovered: 160990
- Ever alive: 30890
- Ever gold: 1150

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
