# SyndProxy private pool

## Current pool

- Alive now: 724
- Gold now: 357
- HTTP: 233 alive / 68 gold
- HTTPS: 123 alive / 18 gold
- SOCKS4: 186 alive / 133 gold
- SOCKS5: 182 alive / 138 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25787
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
