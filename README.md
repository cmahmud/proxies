# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 387
- HTTP: 91 alive / 53 gold
- HTTPS: 50 alive / 13 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 183 alive / 162 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33494
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
