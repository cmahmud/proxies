# SyndProxy private pool

## Current pool

- Alive now: 1167
- Gold now: 508
- HTTP: 410 alive / 171 gold
- HTTPS: 319 alive / 83 gold
- SOCKS4: 232 alive / 128 gold
- SOCKS5: 206 alive / 126 gold

## Historical pool

- Discovered: 127339
- Ever alive: 19767
- Ever gold: 778

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
