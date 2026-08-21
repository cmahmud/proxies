# SyndProxy private pool

## Current pool

- Alive now: 840
- Gold now: 410
- HTTP: 235 alive / 86 gold
- HTTPS: 150 alive / 23 gold
- SOCKS4: 207 alive / 144 gold
- SOCKS5: 248 alive / 157 gold

## Historical pool

- Discovered: 151946
- Ever alive: 27806
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
