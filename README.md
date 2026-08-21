# SyndProxy private pool

## Current pool

- Alive now: 816
- Gold now: 360
- HTTP: 231 alive / 82 gold
- HTTPS: 190 alive / 26 gold
- SOCKS4: 180 alive / 120 gold
- SOCKS5: 215 alive / 132 gold

## Historical pool

- Discovered: 157573
- Ever alive: 29776
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
