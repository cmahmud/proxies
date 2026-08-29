# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 391
- HTTP: 85 alive / 66 gold
- HTTPS: 85 alive / 15 gold
- SOCKS4: 161 alive / 154 gold
- SOCKS5: 172 alive / 156 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43315
- Ever gold: 1369

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
