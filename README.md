# SyndProxy private pool

## Current pool

- Alive now: 1045
- Gold now: 426
- HTTP: 333 alive / 92 gold
- HTTPS: 243 alive / 24 gold
- SOCKS4: 237 alive / 159 gold
- SOCKS5: 232 alive / 151 gold

## Historical pool

- Discovered: 158247
- Ever alive: 30054
- Ever gold: 1140

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
