# SyndProxy private pool

## Current pool

- Alive now: 1850
- Gold now: 658
- HTTP: 710 alive / 214 gold
- HTTPS: 540 alive / 113 gold
- SOCKS4: 248 alive / 159 gold
- SOCKS5: 352 alive / 172 gold

## Historical pool

- Discovered: 141249
- Ever alive: 24170
- Ever gold: 969

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
