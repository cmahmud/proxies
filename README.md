# SyndProxy private pool

## Current pool

- Alive now: 933
- Gold now: 321
- HTTP: 313 alive / 35 gold
- HTTPS: 161 alive / 9 gold
- SOCKS4: 239 alive / 144 gold
- SOCKS5: 220 alive / 133 gold

## Historical pool

- Discovered: 103711
- Ever alive: 14072
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
