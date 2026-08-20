# SyndProxy private pool

## Current pool

- Alive now: 762
- Gold now: 399
- HTTP: 176 alive / 75 gold
- HTTPS: 142 alive / 19 gold
- SOCKS4: 221 alive / 151 gold
- SOCKS5: 223 alive / 154 gold

## Historical pool

- Discovered: 151061
- Ever alive: 27364
- Ever gold: 1095

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
