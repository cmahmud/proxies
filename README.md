# SyndProxy private pool

## Current pool

- Alive now: 776
- Gold now: 399
- HTTP: 185 alive / 89 gold
- HTTPS: 132 alive / 22 gold
- SOCKS4: 229 alive / 138 gold
- SOCKS5: 230 alive / 150 gold

## Historical pool

- Discovered: 154732
- Ever alive: 29177
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
