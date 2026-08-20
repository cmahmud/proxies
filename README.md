# SyndProxy private pool

## Current pool

- Alive now: 766
- Gold now: 403
- HTTP: 171 alive / 78 gold
- HTTPS: 154 alive / 22 gold
- SOCKS4: 219 alive / 152 gold
- SOCKS5: 222 alive / 151 gold

## Historical pool

- Discovered: 149514
- Ever alive: 26963
- Ever gold: 1089

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
