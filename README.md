# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 391
- HTTP: 118 alive / 66 gold
- HTTPS: 61 alive / 14 gold
- SOCKS4: 170 alive / 152 gold
- SOCKS5: 187 alive / 159 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33168
- Ever gold: 1229

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
