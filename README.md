# SyndProxy private pool

## Current pool

- Alive now: 695
- Gold now: 212
- HTTP: 158 alive / 24 gold
- HTTPS: 136 alive / 7 gold
- SOCKS4: 178 alive / 99 gold
- SOCKS5: 223 alive / 82 gold

## Historical pool

- Discovered: 91718
- Ever alive: 8680
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
