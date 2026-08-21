# SyndProxy private pool

## Current pool

- Alive now: 1037
- Gold now: 424
- HTTP: 338 alive / 90 gold
- HTTPS: 233 alive / 23 gold
- SOCKS4: 229 alive / 159 gold
- SOCKS5: 237 alive / 152 gold

## Historical pool

- Discovered: 158247
- Ever alive: 30054
- Ever gold: 1140

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
