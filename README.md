# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 384
- HTTP: 114 alive / 56 gold
- HTTPS: 46 alive / 11 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 178 alive / 160 gold

## Historical pool

- Discovered: 179370
- Ever alive: 33457
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
