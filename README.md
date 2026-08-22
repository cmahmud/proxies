# SyndProxy private pool

## Current pool

- Alive now: 874
- Gold now: 399
- HTTP: 272 alive / 92 gold
- HTTPS: 170 alive / 31 gold
- SOCKS4: 213 alive / 141 gold
- SOCKS5: 219 alive / 135 gold

## Historical pool

- Discovered: 163259
- Ever alive: 31779
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
