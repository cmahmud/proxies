# SyndProxy private pool

## Current pool

- Alive now: 703
- Gold now: 220
- HTTP: 221 alive / 35 gold
- HTTPS: 100 alive / 10 gold
- SOCKS4: 194 alive / 100 gold
- SOCKS5: 188 alive / 75 gold

## Historical pool

- Discovered: 86648
- Ever alive: 5725
- Ever gold: 292

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
