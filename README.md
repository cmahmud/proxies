# SyndProxy private pool

## Current pool

- Alive now: 1092
- Gold now: 536
- HTTP: 384 alive / 160 gold
- HTTPS: 279 alive / 90 gold
- SOCKS4: 221 alive / 155 gold
- SOCKS5: 208 alive / 131 gold

## Historical pool

- Discovered: 119828
- Ever alive: 18216
- Ever gold: 716

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
