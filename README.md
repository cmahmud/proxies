# SyndProxy validated proxy pool

## Current pool

- Alive now: 663
- Gold now: 198
- HTTP: 173 alive / 34 gold
- HTTPS: 41 alive / 6 gold
- SOCKS4: 198 alive / 69 gold
- SOCKS5: 251 alive / 89 gold

## Historical pool

- Discovered: 170566
- Ever alive: 32779
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
