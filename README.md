# SyndProxy private pool

## Current pool

- Alive now: 1134
- Gold now: 549
- HTTP: 417 alive / 185 gold
- HTTPS: 279 alive / 101 gold
- SOCKS4: 207 alive / 120 gold
- SOCKS5: 231 alive / 143 gold

## Historical pool

- Discovered: 124836
- Ever alive: 19264
- Ever gold: 771

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
