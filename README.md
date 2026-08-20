# SyndProxy private pool

## Current pool

- Alive now: 1415
- Gold now: 560
- HTTP: 596 alive / 189 gold
- HTTPS: 385 alive / 95 gold
- SOCKS4: 221 alive / 143 gold
- SOCKS5: 213 alive / 133 gold

## Historical pool

- Discovered: 136255
- Ever alive: 22802
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
