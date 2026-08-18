# SyndProxy private pool

## Current pool

- Alive now: 779
- Gold now: 274
- HTTP: 197 alive / 28 gold
- HTTPS: 143 alive / 4 gold
- SOCKS4: 231 alive / 135 gold
- SOCKS5: 208 alive / 107 gold

## Historical pool

- Discovered: 99957
- Ever alive: 12418
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
