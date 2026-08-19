# SyndProxy private pool

## Current pool

- Alive now: 1008
- Gold now: 538
- HTTP: 349 alive / 170 gold
- HTTPS: 232 alive / 90 gold
- SOCKS4: 210 alive / 136 gold
- SOCKS5: 217 alive / 142 gold

## Historical pool

- Discovered: 122380
- Ever alive: 18651
- Ever gold: 727

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
