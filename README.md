# SyndProxy private pool

## Current pool

- Alive now: 1162
- Gold now: 596
- HTTP: 459 alive / 185 gold
- HTTPS: 267 alive / 109 gold
- SOCKS4: 217 alive / 144 gold
- SOCKS5: 219 alive / 158 gold

## Historical pool

- Discovered: 124852
- Ever alive: 19415
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
