# SyndProxy private pool

## Current pool

- Alive now: 780
- Gold now: 413
- HTTP: 202 alive / 88 gold
- HTTPS: 155 alive / 27 gold
- SOCKS4: 198 alive / 140 gold
- SOCKS5: 225 alive / 158 gold

## Historical pool

- Discovered: 163857
- Ever alive: 31961
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
