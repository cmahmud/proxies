# SyndProxy private pool

## Current pool

- Alive now: 754
- Gold now: 391
- HTTP: 210 alive / 74 gold
- HTTPS: 110 alive / 21 gold
- SOCKS4: 223 alive / 141 gold
- SOCKS5: 211 alive / 155 gold

## Historical pool

- Discovered: 145561
- Ever alive: 25500
- Ever gold: 1063

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
