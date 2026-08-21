# SyndProxy private pool

## Current pool

- Alive now: 1215
- Gold now: 392
- HTTP: 423 alive / 106 gold
- HTTPS: 299 alive / 29 gold
- SOCKS4: 211 alive / 121 gold
- SOCKS5: 282 alive / 136 gold

## Historical pool

- Discovered: 152223
- Ever alive: 27990
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
