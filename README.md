# SyndProxy private pool

## Current pool

- Alive now: 705
- Gold now: 387
- HTTP: 173 alive / 70 gold
- HTTPS: 116 alive / 19 gold
- SOCKS4: 196 alive / 143 gold
- SOCKS5: 220 alive / 155 gold

## Historical pool

- Discovered: 145577
- Ever alive: 25534
- Ever gold: 1063

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
