# SyndProxy private pool

## Current pool

- Alive now: 1143
- Gold now: 581
- HTTP: 414 alive / 174 gold
- HTTPS: 344 alive / 148 gold
- SOCKS4: 201 alive / 125 gold
- SOCKS5: 184 alive / 134 gold

## Historical pool

- Discovered: 127415
- Ever alive: 19960
- Ever gold: 861

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
