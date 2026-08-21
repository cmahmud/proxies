# SyndProxy private pool

## Current pool

- Alive now: 849
- Gold now: 410
- HTTP: 229 alive / 90 gold
- HTTPS: 166 alive / 24 gold
- SOCKS4: 207 alive / 146 gold
- SOCKS5: 247 alive / 150 gold

## Historical pool

- Discovered: 154723
- Ever alive: 29122
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
