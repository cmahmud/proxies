# SyndProxy private pool

## Current pool

- Alive now: 1194
- Gold now: 553
- HTTP: 421 alive / 172 gold
- HTTPS: 342 alive / 81 gold
- SOCKS4: 221 alive / 151 gold
- SOCKS5: 210 alive / 149 gold

## Historical pool

- Discovered: 127339
- Ever alive: 19758
- Ever gold: 777

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
