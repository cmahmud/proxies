# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 396
- HTTP: 123 alive / 61 gold
- HTTPS: 66 alive / 14 gold
- SOCKS4: 172 alive / 157 gold
- SOCKS5: 188 alive / 164 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33527
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
