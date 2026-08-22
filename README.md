# SyndProxy private pool

## Current pool

- Alive now: 946
- Gold now: 434
- HTTP: 295 alive / 89 gold
- HTTPS: 211 alive / 32 gold
- SOCKS4: 197 alive / 150 gold
- SOCKS5: 243 alive / 163 gold

## Historical pool

- Discovered: 162748
- Ever alive: 31533
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
