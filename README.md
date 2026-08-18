# SyndProxy private pool

## Current pool

- Alive now: 616
- Gold now: 236
- HTTP: 193 alive / 30 gold
- HTTPS: 72 alive / 7 gold
- SOCKS4: 184 alive / 112 gold
- SOCKS5: 167 alive / 87 gold

## Historical pool

- Discovered: 86712
- Ever alive: 6455
- Ever gold: 316

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
