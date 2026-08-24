# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 385
- HTTP: 106 alive / 59 gold
- HTTPS: 38 alive / 12 gold
- SOCKS4: 171 alive / 154 gold
- SOCKS5: 181 alive / 160 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33192
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
