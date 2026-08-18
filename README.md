# SyndProxy private pool

## Current pool

- Alive now: 980
- Gold now: 346
- HTTP: 316 alive / 52 gold
- HTTPS: 207 alive / 14 gold
- SOCKS4: 229 alive / 143 gold
- SOCKS5: 228 alive / 137 gold

## Historical pool

- Discovered: 107145
- Ever alive: 15096
- Ever gold: 479

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
