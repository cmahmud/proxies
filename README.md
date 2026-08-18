# SyndProxy private pool

## Current pool

- Alive now: 646
- Gold now: 241
- HTTP: 169 alive / 27 gold
- HTTPS: 85 alive / 9 gold
- SOCKS4: 207 alive / 119 gold
- SOCKS5: 185 alive / 86 gold

## Historical pool

- Discovered: 86739
- Ever alive: 6883
- Ever gold: 334

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
