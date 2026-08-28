# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 368
- HTTP: 89 alive / 67 gold
- HTTPS: 78 alive / 11 gold
- SOCKS4: 165 alive / 144 gold
- SOCKS5: 171 alive / 146 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43182
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
