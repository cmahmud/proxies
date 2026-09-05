# SyndProxy validated proxy pool

## Current pool

- Alive now: 388
- Gold now: 307
- HTTP: 106 alive / 79 gold
- HTTPS: 52 alive / 21 gold
- SOCKS4: 77 alive / 71 gold
- SOCKS5: 153 alive / 136 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47926
- Ever gold: 1504

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
