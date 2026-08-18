# SyndProxy private pool

## Current pool

- Alive now: 862
- Gold now: 286
- HTTP: 262 alive / 28 gold
- HTTPS: 147 alive / 5 gold
- SOCKS4: 234 alive / 144 gold
- SOCKS5: 219 alive / 109 gold

## Historical pool

- Discovered: 99957
- Ever alive: 12372
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
