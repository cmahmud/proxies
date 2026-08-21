# SyndProxy private pool

## Current pool

- Alive now: 866
- Gold now: 411
- HTTP: 241 alive / 90 gold
- HTTPS: 171 alive / 25 gold
- SOCKS4: 210 alive / 148 gold
- SOCKS5: 244 alive / 148 gold

## Historical pool

- Discovered: 154723
- Ever alive: 29117
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
