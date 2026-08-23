# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 387
- HTTP: 129 alive / 61 gold
- HTTPS: 57 alive / 13 gold
- SOCKS4: 181 alive / 154 gold
- SOCKS5: 190 alive / 159 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33192
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
