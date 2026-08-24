# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 387
- HTTP: 93 alive / 49 gold
- HTTPS: 39 alive / 12 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33543
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
