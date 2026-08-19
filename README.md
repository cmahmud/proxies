# SyndProxy private pool

## Current pool

- Alive now: 1012
- Gold now: 507
- HTTP: 342 alive / 159 gold
- HTTPS: 258 alive / 91 gold
- SOCKS4: 212 alive / 140 gold
- SOCKS5: 200 alive / 117 gold

## Historical pool

- Discovered: 119845
- Ever alive: 18374
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
