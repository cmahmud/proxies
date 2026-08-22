# SyndProxy private pool

## Current pool

- Alive now: 794
- Gold now: 401
- HTTP: 213 alive / 93 gold
- HTTPS: 167 alive / 28 gold
- SOCKS4: 192 alive / 127 gold
- SOCKS5: 222 alive / 153 gold

## Historical pool

- Discovered: 162003
- Ever alive: 31378
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
