# SyndProxy private pool

## Current pool

- Alive now: 779
- Gold now: 268
- HTTP: 218 alive / 27 gold
- HTTPS: 144 alive / 3 gold
- SOCKS4: 221 alive / 134 gold
- SOCKS5: 196 alive / 104 gold

## Historical pool

- Discovered: 99079
- Ever alive: 11453
- Ever gold: 383

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
