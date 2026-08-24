# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 427
- HTTP: 131 alive / 78 gold
- HTTPS: 64 alive / 22 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 186 alive / 167 gold

## Historical pool

- Discovered: 181494
- Ever alive: 33940
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
