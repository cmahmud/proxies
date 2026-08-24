# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 387
- HTTP: 98 alive / 55 gold
- HTTPS: 37 alive / 13 gold
- SOCKS4: 176 alive / 158 gold
- SOCKS5: 183 alive / 161 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33481
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
