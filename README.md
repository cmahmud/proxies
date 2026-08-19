# SyndProxy private pool

## Current pool

- Alive now: 890
- Gold now: 300
- HTTP: 316 alive / 66 gold
- HTTPS: 219 alive / 18 gold
- SOCKS4: 184 alive / 117 gold
- SOCKS5: 171 alive / 99 gold

## Historical pool

- Discovered: 109991
- Ever alive: 15648
- Ever gold: 499

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
