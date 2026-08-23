# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 391
- HTTP: 143 alive / 64 gold
- HTTPS: 67 alive / 13 gold
- SOCKS4: 186 alive / 154 gold
- SOCKS5: 192 alive / 160 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33187
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
