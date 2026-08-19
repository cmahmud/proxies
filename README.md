# SyndProxy private pool

## Current pool

- Alive now: 995
- Gold now: 487
- HTTP: 325 alive / 145 gold
- HTTPS: 258 alive / 88 gold
- SOCKS4: 202 alive / 122 gold
- SOCKS5: 210 alive / 132 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17602
- Ever gold: 690

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
