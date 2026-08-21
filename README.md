# SyndProxy private pool

## Current pool

- Alive now: 934
- Gold now: 412
- HTTP: 264 alive / 92 gold
- HTTPS: 198 alive / 25 gold
- SOCKS4: 225 alive / 146 gold
- SOCKS5: 247 alive / 149 gold

## Historical pool

- Discovered: 154723
- Ever alive: 29092
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
