# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 380
- HTTP: 94 alive / 64 gold
- HTTPS: 49 alive / 12 gold
- SOCKS4: 159 alive / 150 gold
- SOCKS5: 176 alive / 154 gold

## Historical pool

- Discovered: 174159
- Ever alive: 33076
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
