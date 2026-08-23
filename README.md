# SyndProxy validated proxy pool

## Current pool

- Alive now: 655
- Gold now: 201
- HTTP: 159 alive / 35 gold
- HTTPS: 42 alive / 6 gold
- SOCKS4: 208 alive / 69 gold
- SOCKS5: 246 alive / 91 gold

## Historical pool

- Discovered: 170570
- Ever alive: 32779
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
