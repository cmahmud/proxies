# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 389
- HTTP: 118 alive / 67 gold
- HTTPS: 51 alive / 13 gold
- SOCKS4: 162 alive / 152 gold
- SOCKS5: 207 alive / 157 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33178
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
