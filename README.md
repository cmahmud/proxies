# SyndProxy private pool

## Current pool

- Alive now: 862
- Gold now: 260
- HTTP: 274 alive / 27 gold
- HTTPS: 146 alive / 3 gold
- SOCKS4: 221 alive / 119 gold
- SOCKS5: 221 alive / 111 gold

## Historical pool

- Discovered: 99142
- Ever alive: 12047
- Ever gold: 390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
