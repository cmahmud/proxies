# SyndProxy private pool

## Current pool

- Alive now: 931
- Gold now: 406
- HTTP: 270 alive / 77 gold
- HTTPS: 203 alive / 26 gold
- SOCKS4: 213 alive / 155 gold
- SOCKS5: 245 alive / 148 gold

## Historical pool

- Discovered: 165846
- Ever alive: 32373
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
