# SyndProxy private pool

## Current pool

- Alive now: 1779
- Gold now: 663
- HTTP: 652 alive / 216 gold
- HTTPS: 526 alive / 116 gold
- SOCKS4: 244 alive / 160 gold
- SOCKS5: 357 alive / 171 gold

## Historical pool

- Discovered: 141249
- Ever alive: 24161
- Ever gold: 969

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
