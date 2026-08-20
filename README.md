# SyndProxy private pool

## Current pool

- Alive now: 685
- Gold now: 387
- HTTP: 168 alive / 67 gold
- HTTPS: 90 alive / 16 gold
- SOCKS4: 198 alive / 142 gold
- SOCKS5: 229 alive / 162 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25792
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
