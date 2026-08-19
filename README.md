# SyndProxy private pool

## Current pool

- Alive now: 1276
- Gold now: 375
- HTTP: 419 alive / 86 gold
- HTTPS: 292 alive / 20 gold
- SOCKS4: 242 alive / 127 gold
- SOCKS5: 323 alive / 142 gold

## Historical pool

- Discovered: 134551
- Ever alive: 22042
- Ever gold: 891

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
