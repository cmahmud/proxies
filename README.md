# SyndProxy private pool

## Current pool

- Alive now: 1034
- Gold now: 519
- HTTP: 371 alive / 165 gold
- HTTPS: 243 alive / 92 gold
- SOCKS4: 199 alive / 127 gold
- SOCKS5: 221 alive / 135 gold

## Historical pool

- Discovered: 123164
- Ever alive: 18775
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
