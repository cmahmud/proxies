# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 336
- HTTP: 112 alive / 39 gold
- HTTPS: 69 alive / 9 gold
- SOCKS4: 169 alive / 149 gold
- SOCKS5: 176 alive / 139 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32792
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
