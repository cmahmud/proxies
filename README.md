# SyndProxy private pool

## Current pool

- Alive now: 779
- Gold now: 275
- HTTP: 190 alive / 28 gold
- HTTPS: 144 alive / 5 gold
- SOCKS4: 233 alive / 135 gold
- SOCKS5: 212 alive / 107 gold

## Historical pool

- Discovered: 99957
- Ever alive: 12410
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
