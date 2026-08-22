# SyndProxy private pool

## Current pool

- Alive now: 762
- Gold now: 410
- HTTP: 197 alive / 83 gold
- HTTPS: 145 alive / 28 gold
- SOCKS4: 209 alive / 140 gold
- SOCKS5: 211 alive / 159 gold

## Historical pool

- Discovered: 162441
- Ever alive: 31429
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
