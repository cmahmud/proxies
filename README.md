# SyndProxy private pool

## Current pool

- Alive now: 891
- Gold now: 228
- HTTP: 278 alive / 29 gold
- HTTPS: 155 alive / 8 gold
- SOCKS4: 241 alive / 110 gold
- SOCKS5: 217 alive / 81 gold

## Historical pool

- Discovered: 86774
- Ever alive: 7592
- Ever gold: 337

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
