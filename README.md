# SyndProxy private pool

## Current pool

- Alive now: 1042
- Gold now: 378
- HTTP: 352 alive / 93 gold
- HTTPS: 269 alive / 29 gold
- SOCKS4: 186 alive / 120 gold
- SOCKS5: 235 alive / 136 gold

## Historical pool

- Discovered: 153749
- Ever alive: 28827
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
