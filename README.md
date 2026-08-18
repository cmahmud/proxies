# SyndProxy private pool

## Current pool

- Alive now: 1077
- Gold now: 350
- HTTP: 398 alive / 51 gold
- HTTPS: 221 alive / 13 gold
- SOCKS4: 222 alive / 141 gold
- SOCKS5: 236 alive / 145 gold

## Historical pool

- Discovered: 107115
- Ever alive: 14860
- Ever gold: 475

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
