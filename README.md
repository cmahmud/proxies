# SyndProxy private pool

## Current pool

- Alive now: 942
- Gold now: 479
- HTTP: 293 alive / 123 gold
- HTTPS: 230 alive / 90 gold
- SOCKS4: 192 alive / 128 gold
- SOCKS5: 227 alive / 138 gold

## Historical pool

- Discovered: 117147
- Ever alive: 17560
- Ever gold: 671

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
