# SyndProxy private pool

## Current pool

- Alive now: 1173
- Gold now: 500
- HTTP: 408 alive / 148 gold
- HTTPS: 288 alive / 91 gold
- SOCKS4: 227 alive / 123 gold
- SOCKS5: 250 alive / 138 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17282
- Ever gold: 661

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
