# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 401
- HTTP: 87 alive / 58 gold
- HTTPS: 40 alive / 15 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 180 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42848
- Ever gold: 1363

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
