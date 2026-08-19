# SyndProxy private pool

## Current pool

- Alive now: 1163
- Gold now: 507
- HTTP: 458 alive / 175 gold
- HTTPS: 310 alive / 114 gold
- SOCKS4: 209 alive / 105 gold
- SOCKS5: 186 alive / 113 gold

## Historical pool

- Discovered: 124843
- Ever alive: 19330
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
