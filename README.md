# SyndProxy private pool

## Current pool

- Alive now: 774
- Gold now: 392
- HTTP: 240 alive / 90 gold
- HTTPS: 113 alive / 25 gold
- SOCKS4: 188 alive / 120 gold
- SOCKS5: 233 alive / 157 gold

## Historical pool

- Discovered: 156417
- Ever alive: 29468
- Ever gold: 1128

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
