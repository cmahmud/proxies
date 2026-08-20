# SyndProxy private pool

## Current pool

- Alive now: 1735
- Gold now: 661
- HTTP: 635 alive / 214 gold
- HTTPS: 507 alive / 116 gold
- SOCKS4: 241 alive / 160 gold
- SOCKS5: 352 alive / 171 gold

## Historical pool

- Discovered: 141249
- Ever alive: 24158
- Ever gold: 969

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
