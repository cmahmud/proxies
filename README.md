# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 403
- HTTP: 77 alive / 60 gold
- HTTPS: 75 alive / 14 gold
- SOCKS4: 180 alive / 165 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41566
- Ever gold: 1339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
