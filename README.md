# SyndProxy validated proxy pool

## Current pool

- Alive now: 693
- Gold now: 200
- HTTP: 164 alive / 35 gold
- HTTPS: 46 alive / 6 gold
- SOCKS4: 237 alive / 68 gold
- SOCKS5: 246 alive / 91 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32779
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
