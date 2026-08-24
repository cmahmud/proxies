# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 386
- HTTP: 88 alive / 51 gold
- HTTPS: 47 alive / 14 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 183 alive / 162 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33492
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
