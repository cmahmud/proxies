# SyndProxy private pool

## Current pool

- Alive now: 699
- Gold now: 217
- HTTP: 219 alive / 33 gold
- HTTPS: 100 alive / 10 gold
- SOCKS4: 194 alive / 101 gold
- SOCKS5: 186 alive / 73 gold

## Historical pool

- Discovered: 86648
- Ever alive: 5725
- Ever gold: 292

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
