# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 439
- HTTP: 108 alive / 77 gold
- HTTPS: 50 alive / 28 gold
- SOCKS4: 185 alive / 165 gold
- SOCKS5: 176 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49118
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
