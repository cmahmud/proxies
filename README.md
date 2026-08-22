# SyndProxy private pool

## Current pool

- Alive now: 831
- Gold now: 412
- HTTP: 232 alive / 83 gold
- HTTPS: 166 alive / 27 gold
- SOCKS4: 181 alive / 133 gold
- SOCKS5: 252 alive / 169 gold

## Historical pool

- Discovered: 162742
- Ever alive: 31478
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
