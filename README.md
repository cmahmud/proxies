# SyndProxy validated proxy pool

## Current pool

- Alive now: 686
- Gold now: 197
- HTTP: 195 alive / 35 gold
- HTTPS: 42 alive / 6 gold
- SOCKS4: 191 alive / 68 gold
- SOCKS5: 258 alive / 88 gold

## Historical pool

- Discovered: 170566
- Ever alive: 32779
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
