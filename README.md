# SyndProxy private pool

## Current pool

- Alive now: 1376
- Gold now: 584
- HTTP: 482 alive / 194 gold
- HTTPS: 370 alive / 100 gold
- SOCKS4: 250 alive / 141 gold
- SOCKS5: 274 alive / 149 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23292
- Ever gold: 916

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
