# SyndProxy private pool

## Current pool

- Alive now: 782
- Gold now: 391
- HTTP: 215 alive / 79 gold
- HTTPS: 171 alive / 23 gold
- SOCKS4: 207 alive / 147 gold
- SOCKS5: 189 alive / 142 gold

## Historical pool

- Discovered: 149514
- Ever alive: 26928
- Ever gold: 1089

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
