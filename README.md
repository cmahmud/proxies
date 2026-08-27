# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 403
- HTTP: 78 alive / 57 gold
- HTTPS: 51 alive / 18 gold
- SOCKS4: 177 alive / 164 gold
- SOCKS5: 183 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41597
- Ever gold: 1339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
