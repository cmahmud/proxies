# SyndProxy private pool

## Current pool

- Alive now: 958
- Gold now: 402
- HTTP: 282 alive / 90 gold
- HTTPS: 209 alive / 25 gold
- SOCKS4: 216 alive / 133 gold
- SOCKS5: 251 alive / 154 gold

## Historical pool

- Discovered: 161993
- Ever alive: 31334
- Ever gold: 1157

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
