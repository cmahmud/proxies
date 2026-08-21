# SyndProxy private pool

## Current pool

- Alive now: 757
- Gold now: 405
- HTTP: 216 alive / 92 gold
- HTTPS: 141 alive / 25 gold
- SOCKS4: 186 alive / 128 gold
- SOCKS5: 214 alive / 160 gold

## Historical pool

- Discovered: 151684
- Ever alive: 27691
- Ever gold: 1102

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
