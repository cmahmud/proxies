# SyndProxy private pool

## Current pool

- Alive now: 854
- Gold now: 281
- HTTP: 286 alive / 40 gold
- HTTPS: 167 alive / 8 gold
- SOCKS4: 223 alive / 141 gold
- SOCKS5: 178 alive / 92 gold

## Historical pool

- Discovered: 102887
- Ever alive: 13807
- Ever gold: 430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
