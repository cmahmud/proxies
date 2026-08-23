# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 392
- HTTP: 108 alive / 67 gold
- HTTPS: 50 alive / 14 gold
- SOCKS4: 158 alive / 152 gold
- SOCKS5: 192 alive / 159 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33178
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
