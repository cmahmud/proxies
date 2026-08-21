# SyndProxy private pool

## Current pool

- Alive now: 1119
- Gold now: 410
- HTTP: 360 alive / 94 gold
- HTTPS: 283 alive / 36 gold
- SOCKS4: 243 alive / 146 gold
- SOCKS5: 233 alive / 134 gold

## Historical pool

- Discovered: 161002
- Ever alive: 30983
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
