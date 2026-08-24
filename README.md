# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 386
- HTTP: 81 alive / 55 gold
- HTTPS: 44 alive / 13 gold
- SOCKS4: 174 alive / 157 gold
- SOCKS5: 183 alive / 161 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33483
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
