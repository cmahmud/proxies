# SyndProxy private pool

## Current pool

- Alive now: 1043
- Gold now: 507
- HTTP: 371 alive / 157 gold
- HTTPS: 249 alive / 91 gold
- SOCKS4: 220 alive / 141 gold
- SOCKS5: 203 alive / 118 gold

## Historical pool

- Discovered: 119845
- Ever alive: 18374
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
