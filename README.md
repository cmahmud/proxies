# SyndProxy private pool

## Current pool

- Alive now: 1193
- Gold now: 501
- HTTP: 412 alive / 145 gold
- HTTPS: 332 alive / 93 gold
- SOCKS4: 203 alive / 123 gold
- SOCKS5: 246 alive / 140 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17339
- Ever gold: 663

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
