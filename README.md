# SyndProxy private pool

## Current pool

- Alive now: 737
- Gold now: 386
- HTTP: 201 alive / 78 gold
- HTTPS: 113 alive / 20 gold
- SOCKS4: 222 alive / 143 gold
- SOCKS5: 201 alive / 145 gold

## Historical pool

- Discovered: 144750
- Ever alive: 25241
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
