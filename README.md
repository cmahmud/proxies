# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 413
- HTTP: 105 alive / 68 gold
- HTTPS: 134 alive / 17 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 188 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41289
- Ever gold: 1320

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
