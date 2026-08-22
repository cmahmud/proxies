# SyndProxy private pool

## Current pool

- Alive now: 886
- Gold now: 412
- HTTP: 282 alive / 83 gold
- HTTPS: 169 alive / 25 gold
- SOCKS4: 183 alive / 133 gold
- SOCKS5: 252 alive / 171 gold

## Historical pool

- Discovered: 162742
- Ever alive: 31476
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
