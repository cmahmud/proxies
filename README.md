# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 466
- HTTP: 134 alive / 94 gold
- HTTPS: 108 alive / 35 gold
- SOCKS4: 183 alive / 161 gold
- SOCKS5: 207 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46399
- Ever gold: 1444

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
