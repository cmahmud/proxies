# SyndProxy private pool

## Current pool

- Alive now: 1164
- Gold now: 414
- HTTP: 388 alive / 84 gold
- HTTPS: 244 alive / 15 gold
- SOCKS4: 265 alive / 155 gold
- SOCKS5: 267 alive / 160 gold

## Historical pool

- Discovered: 131722
- Ever alive: 20779
- Ever gold: 875

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
