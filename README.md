# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 396
- HTTP: 106 alive / 68 gold
- HTTPS: 43 alive / 14 gold
- SOCKS4: 159 alive / 154 gold
- SOCKS5: 206 alive / 160 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33182
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
