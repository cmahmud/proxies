# SyndProxy private pool

## Current pool

- Alive now: 1071
- Gold now: 543
- HTTP: 371 alive / 165 gold
- HTTPS: 249 alive / 94 gold
- SOCKS4: 240 alive / 144 gold
- SOCKS5: 211 alive / 140 gold

## Historical pool

- Discovered: 123170
- Ever alive: 18873
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
