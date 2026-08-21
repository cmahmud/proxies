# SyndProxy private pool

## Current pool

- Alive now: 847
- Gold now: 430
- HTTP: 241 alive / 85 gold
- HTTPS: 120 alive / 25 gold
- SOCKS4: 231 alive / 154 gold
- SOCKS5: 255 alive / 166 gold

## Historical pool

- Discovered: 157420
- Ever alive: 29746
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
