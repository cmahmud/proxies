# SyndProxy validated proxy pool

## Current pool

- Alive now: 681
- Gold now: 197
- HTTP: 183 alive / 34 gold
- HTTPS: 41 alive / 6 gold
- SOCKS4: 195 alive / 69 gold
- SOCKS5: 262 alive / 88 gold

## Historical pool

- Discovered: 170566
- Ever alive: 32779
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
