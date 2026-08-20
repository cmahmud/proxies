# SyndProxy private pool

## Current pool

- Alive now: 779
- Gold now: 393
- HTTP: 221 alive / 82 gold
- HTTPS: 135 alive / 22 gold
- SOCKS4: 215 alive / 143 gold
- SOCKS5: 208 alive / 146 gold

## Historical pool

- Discovered: 144750
- Ever alive: 25263
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
