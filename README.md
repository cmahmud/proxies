# SyndProxy private pool

## Current pool

- Alive now: 875
- Gold now: 403
- HTTP: 247 alive / 90 gold
- HTTPS: 189 alive / 26 gold
- SOCKS4: 202 alive / 133 gold
- SOCKS5: 237 alive / 154 gold

## Historical pool

- Discovered: 161993
- Ever alive: 31334
- Ever gold: 1157

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
