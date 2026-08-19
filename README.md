# SyndProxy private pool

## Current pool

- Alive now: 1047
- Gold now: 524
- HTTP: 351 alive / 163 gold
- HTTPS: 288 alive / 92 gold
- SOCKS4: 203 alive / 140 gold
- SOCKS5: 205 alive / 129 gold

## Historical pool

- Discovered: 119846
- Ever alive: 18421
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
