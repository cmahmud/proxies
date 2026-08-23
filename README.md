# SyndProxy validated proxy pool

## Current pool

- Alive now: 330
- Gold now: 205
- HTTP: 102 alive / 47 gold
- HTTPS: 37 alive / 6 gold
- SOCKS4: 83 alive / 64 gold
- SOCKS5: 108 alive / 88 gold

## Historical pool

- Discovered: 170533
- Ever alive: 32758
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
