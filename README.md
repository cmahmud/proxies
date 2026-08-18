# SyndProxy private pool

## Current pool

- Alive now: 937
- Gold now: 248
- HTTP: 302 alive / 32 gold
- HTTPS: 226 alive / 7 gold
- SOCKS4: 247 alive / 143 gold
- SOCKS5: 162 alive / 66 gold

## Historical pool

- Discovered: 102887
- Ever alive: 13748
- Ever gold: 429

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
