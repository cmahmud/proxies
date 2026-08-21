# SyndProxy private pool

## Current pool

- Alive now: 1102
- Gold now: 428
- HTTP: 380 alive / 108 gold
- HTTPS: 242 alive / 26 gold
- SOCKS4: 236 alive / 154 gold
- SOCKS5: 244 alive / 140 gold

## Historical pool

- Discovered: 160024
- Ever alive: 30554
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
