# SyndProxy private pool

## Current pool

- Alive now: 966
- Gold now: 414
- HTTP: 297 alive / 93 gold
- HTTPS: 242 alive / 24 gold
- SOCKS4: 190 alive / 129 gold
- SOCKS5: 237 alive / 168 gold

## Historical pool

- Discovered: 144729
- Ever alive: 24912
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
