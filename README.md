# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 420
- HTTP: 94 alive / 74 gold
- HTTPS: 96 alive / 22 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 176 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41779
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
