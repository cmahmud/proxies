# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 386
- HTTP: 109 alive / 61 gold
- HTTPS: 45 alive / 12 gold
- SOCKS4: 174 alive / 154 gold
- SOCKS5: 182 alive / 159 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33192
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
