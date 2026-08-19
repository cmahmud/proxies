# SyndProxy private pool

## Current pool

- Alive now: 1172
- Gold now: 549
- HTTP: 470 alive / 192 gold
- HTTPS: 294 alive / 115 gold
- SOCKS4: 209 alive / 113 gold
- SOCKS5: 199 alive / 129 gold

## Historical pool

- Discovered: 124850
- Ever alive: 19400
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
