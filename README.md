# SyndProxy private pool

## Current pool

- Alive now: 790
- Gold now: 221
- HTTP: 243 alive / 32 gold
- HTTPS: 145 alive / 9 gold
- SOCKS4: 200 alive / 111 gold
- SOCKS5: 202 alive / 69 gold

## Historical pool

- Discovered: 94321
- Ever alive: 9327
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
