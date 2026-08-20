# SyndProxy private pool

## Current pool

- Alive now: 663
- Gold now: 346
- HTTP: 174 alive / 71 gold
- HTTPS: 115 alive / 18 gold
- SOCKS4: 178 alive / 121 gold
- SOCKS5: 196 alive / 136 gold

## Historical pool

- Discovered: 145577
- Ever alive: 25573
- Ever gold: 1066

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
