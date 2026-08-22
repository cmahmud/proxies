# SyndProxy private pool

## Current pool

- Alive now: 779
- Gold now: 390
- HTTP: 203 alive / 89 gold
- HTTPS: 150 alive / 23 gold
- SOCKS4: 191 alive / 127 gold
- SOCKS5: 235 alive / 151 gold

## Historical pool

- Discovered: 162003
- Ever alive: 31386
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
