# SyndProxy private pool

## Current pool

- Alive now: 1042
- Gold now: 397
- HTTP: 293 alive / 72 gold
- HTTPS: 225 alive / 12 gold
- SOCKS4: 254 alive / 153 gold
- SOCKS5: 270 alive / 160 gold

## Historical pool

- Discovered: 131115
- Ever alive: 20600
- Ever gold: 869

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
