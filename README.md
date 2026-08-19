# SyndProxy private pool

## Current pool

- Alive now: 1028
- Gold now: 538
- HTTP: 358 alive / 170 gold
- HTTPS: 240 alive / 90 gold
- SOCKS4: 209 alive / 136 gold
- SOCKS5: 221 alive / 142 gold

## Historical pool

- Discovered: 122380
- Ever alive: 18651
- Ever gold: 727

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
