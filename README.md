# SyndProxy private pool

## Current pool

- Alive now: 936
- Gold now: 344
- HTTP: 308 alive / 65 gold
- HTTPS: 192 alive / 15 gold
- SOCKS4: 229 alive / 141 gold
- SOCKS5: 207 alive / 123 gold

## Historical pool

- Discovered: 109955
- Ever alive: 15307
- Ever gold: 491

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
