# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 429
- HTTP: 121 alive / 80 gold
- HTTPS: 73 alive / 21 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 187 alive / 169 gold

## Historical pool

- Discovered: 181494
- Ever alive: 33935
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
