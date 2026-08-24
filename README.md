# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 385
- HTTP: 82 alive / 55 gold
- HTTPS: 47 alive / 13 gold
- SOCKS4: 174 alive / 157 gold
- SOCKS5: 184 alive / 160 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33483
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
