# SyndProxy private pool

## Current pool

- Alive now: 1460
- Gold now: 555
- HTTP: 585 alive / 175 gold
- HTTPS: 408 alive / 91 gold
- SOCKS4: 220 alive / 131 gold
- SOCKS5: 247 alive / 158 gold

## Historical pool

- Discovered: 138827
- Ever alive: 23037
- Ever gold: 913

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
