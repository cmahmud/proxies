# SyndProxy private pool

## Current pool

- Alive now: 1135
- Gold now: 542
- HTTP: 410 alive / 164 gold
- HTTPS: 277 alive / 92 gold
- SOCKS4: 217 alive / 133 gold
- SOCKS5: 231 alive / 153 gold

## Historical pool

- Discovered: 123164
- Ever alive: 18757
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
