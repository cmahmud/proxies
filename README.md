# SyndProxy private pool

## Current pool

- Alive now: 852
- Gold now: 284
- HTTP: 257 alive / 26 gold
- HTTPS: 141 alive / 5 gold
- SOCKS4: 236 alive / 144 gold
- SOCKS5: 218 alive / 109 gold

## Historical pool

- Discovered: 99957
- Ever alive: 12371
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
