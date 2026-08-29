# SyndProxy validated proxy pool

## Current pool

- Alive now: 339
- Gold now: 281
- HTTP: 34 alive / 19 gold
- HTTPS: 4 alive / 0 gold
- SOCKS4: 152 alive / 145 gold
- SOCKS5: 149 alive / 117 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43625
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
