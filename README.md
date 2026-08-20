# SyndProxy private pool

## Current pool

- Alive now: 1410
- Gold now: 578
- HTTP: 579 alive / 188 gold
- HTTPS: 344 alive / 91 gold
- SOCKS4: 228 alive / 140 gold
- SOCKS5: 259 alive / 159 gold

## Historical pool

- Discovered: 138940
- Ever alive: 23145
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
