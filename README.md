# SyndProxy private pool

## Current pool

- Alive now: 1113
- Gold now: 290
- HTTP: 458 alive / 28 gold
- HTTPS: 178 alive / 7 gold
- SOCKS4: 237 alive / 130 gold
- SOCKS5: 240 alive / 125 gold

## Historical pool

- Discovered: 102839
- Ever alive: 13121
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
