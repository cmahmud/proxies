# SyndProxy validated proxy pool

## Current pool

- Alive now: 683
- Gold now: 200
- HTTP: 160 alive / 35 gold
- HTTPS: 53 alive / 6 gold
- SOCKS4: 230 alive / 68 gold
- SOCKS5: 240 alive / 91 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32779
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
