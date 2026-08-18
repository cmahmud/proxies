# SyndProxy private pool

## Current pool

- Alive now: 845
- Gold now: 258
- HTTP: 254 alive / 28 gold
- HTTPS: 154 alive / 3 gold
- SOCKS4: 212 alive / 118 gold
- SOCKS5: 225 alive / 109 gold

## Historical pool

- Discovered: 99142
- Ever alive: 12063
- Ever gold: 390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
