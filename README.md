# SyndProxy validated proxy pool

## Current pool

- Alive now: 583
- Gold now: 389
- HTTP: 141 alive / 62 gold
- HTTPS: 69 alive / 14 gold
- SOCKS4: 187 alive / 154 gold
- SOCKS5: 186 alive / 159 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33188
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
