# SyndProxy private pool

## Current pool

- Alive now: 1141
- Gold now: 588
- HTTP: 412 alive / 172 gold
- HTTPS: 313 alive / 145 gold
- SOCKS4: 224 alive / 143 gold
- SOCKS5: 192 alive / 128 gold

## Historical pool

- Discovered: 127415
- Ever alive: 19960
- Ever gold: 861

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
