# SyndProxy private pool

## Current pool

- Alive now: 1083
- Gold now: 479
- HTTP: 398 alive / 127 gold
- HTTPS: 262 alive / 77 gold
- SOCKS4: 210 alive / 122 gold
- SOCKS5: 213 alive / 153 gold

## Historical pool

- Discovered: 119696
- Ever alive: 17875
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
