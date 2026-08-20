# SyndProxy private pool

## Current pool

- Alive now: 779
- Gold now: 418
- HTTP: 197 alive / 80 gold
- HTTPS: 150 alive / 29 gold
- SOCKS4: 215 alive / 149 gold
- SOCKS5: 217 alive / 160 gold

## Historical pool

- Discovered: 151059
- Ever alive: 27324
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
