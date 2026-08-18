# SyndProxy private pool

## Current pool

- Alive now: 873
- Gold now: 288
- HTTP: 264 alive / 29 gold
- HTTPS: 148 alive / 5 gold
- SOCKS4: 242 alive / 144 gold
- SOCKS5: 219 alive / 110 gold

## Historical pool

- Discovered: 99957
- Ever alive: 12372
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
