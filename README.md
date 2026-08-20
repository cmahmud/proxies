# SyndProxy private pool

## Current pool

- Alive now: 993
- Gold now: 394
- HTTP: 318 alive / 83 gold
- HTTPS: 230 alive / 23 gold
- SOCKS4: 197 alive / 133 gold
- SOCKS5: 248 alive / 155 gold

## Historical pool

- Discovered: 144732
- Ever alive: 24975
- Ever gold: 1052

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
