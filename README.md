# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 409
- HTTP: 101 alive / 60 gold
- HTTPS: 157 alive / 16 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 194 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40779
- Ever gold: 1312

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
