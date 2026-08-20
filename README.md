# SyndProxy private pool

## Current pool

- Alive now: 726
- Gold now: 381
- HTTP: 180 alive / 79 gold
- HTTPS: 137 alive / 19 gold
- SOCKS4: 213 alive / 143 gold
- SOCKS5: 196 alive / 140 gold

## Historical pool

- Discovered: 149512
- Ever alive: 26900
- Ever gold: 1089

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
