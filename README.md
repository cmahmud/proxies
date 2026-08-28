# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 402
- HTTP: 102 alive / 74 gold
- HTTPS: 80 alive / 13 gold
- SOCKS4: 162 alive / 155 gold
- SOCKS5: 174 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43079
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
