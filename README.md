# SyndProxy private pool

## Current pool

- Alive now: 712
- Gold now: 377
- HTTP: 182 alive / 72 gold
- HTTPS: 117 alive / 19 gold
- SOCKS4: 214 alive / 145 gold
- SOCKS5: 199 alive / 141 gold

## Historical pool

- Discovered: 148340
- Ever alive: 26365
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
