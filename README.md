# SyndProxy private pool

## Current pool

- Alive now: 960
- Gold now: 495
- HTTP: 309 alive / 146 gold
- HTTPS: 242 alive / 90 gold
- SOCKS4: 192 alive / 124 gold
- SOCKS5: 217 alive / 135 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17598
- Ever gold: 690

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
