# SyndProxy private pool

## Current pool

- Alive now: 1027
- Gold now: 402
- HTTP: 292 alive / 74 gold
- HTTPS: 209 alive / 14 gold
- SOCKS4: 259 alive / 153 gold
- SOCKS5: 267 alive / 161 gold

## Historical pool

- Discovered: 131115
- Ever alive: 20591
- Ever gold: 869

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
