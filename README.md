# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 439
- HTTP: 102 alive / 78 gold
- HTTPS: 49 alive / 27 gold
- SOCKS4: 187 alive / 165 gold
- SOCKS5: 177 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49118
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
