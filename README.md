# SyndProxy private pool

## Current pool

- Alive now: 866
- Gold now: 281
- HTTP: 292 alive / 40 gold
- HTTPS: 195 alive / 8 gold
- SOCKS4: 216 alive / 140 gold
- SOCKS5: 163 alive / 93 gold

## Historical pool

- Discovered: 102887
- Ever alive: 13779
- Ever gold: 430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
