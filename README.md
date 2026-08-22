# SyndProxy private pool

## Current pool

- Alive now: 820
- Gold now: 403
- HTTP: 223 alive / 89 gold
- HTTPS: 154 alive / 30 gold
- SOCKS4: 210 alive / 130 gold
- SOCKS5: 233 alive / 154 gold

## Historical pool

- Discovered: 163842
- Ever alive: 31928
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
