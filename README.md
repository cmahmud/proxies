# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 451
- HTTP: 130 alive / 84 gold
- HTTPS: 124 alive / 38 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 207 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44779
- Ever gold: 1413

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
