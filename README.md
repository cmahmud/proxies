# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 389
- HTTP: 113 alive / 66 gold
- HTTPS: 51 alive / 14 gold
- SOCKS4: 163 alive / 152 gold
- SOCKS5: 209 alive / 157 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33178
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
