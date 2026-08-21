# SyndProxy private pool

## Current pool

- Alive now: 821
- Gold now: 360
- HTTP: 268 alive / 101 gold
- HTTPS: 153 alive / 23 gold
- SOCKS4: 197 alive / 131 gold
- SOCKS5: 203 alive / 105 gold

## Historical pool

- Discovered: 154658
- Ever alive: 28956
- Ever gold: 1117

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
