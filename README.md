# SyndProxy private pool

## Current pool

- Alive now: 1181
- Gold now: 394
- HTTP: 381 alive / 90 gold
- HTTPS: 233 alive / 17 gold
- SOCKS4: 246 alive / 144 gold
- SOCKS5: 321 alive / 143 gold

## Historical pool

- Discovered: 133967
- Ever alive: 21723
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
