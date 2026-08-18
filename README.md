# SyndProxy private pool

## Current pool

- Alive now: 969
- Gold now: 366
- HTTP: 301 alive / 59 gold
- HTTPS: 212 alive / 14 gold
- SOCKS4: 233 alive / 151 gold
- SOCKS5: 223 alive / 142 gold

## Historical pool

- Discovered: 109944
- Ever alive: 15183
- Ever gold: 488

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
