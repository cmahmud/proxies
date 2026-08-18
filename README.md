# SyndProxy private pool

## Current pool

- Alive now: 712
- Gold now: 213
- HTTP: 175 alive / 25 gold
- HTTPS: 137 alive / 7 gold
- SOCKS4: 178 alive / 99 gold
- SOCKS5: 222 alive / 82 gold

## Historical pool

- Discovered: 91718
- Ever alive: 8680
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
