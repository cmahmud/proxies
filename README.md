# SyndProxy private pool

## Current pool

- Alive now: 1059
- Gold now: 507
- HTTP: 381 alive / 149 gold
- HTTPS: 278 alive / 85 gold
- SOCKS4: 181 alive / 117 gold
- SOCKS5: 219 alive / 156 gold

## Historical pool

- Discovered: 118125
- Ever alive: 17782
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
