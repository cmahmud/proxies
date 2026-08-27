# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 410
- HTTP: 100 alive / 60 gold
- HTTPS: 160 alive / 17 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 192 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40779
- Ever gold: 1312

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
