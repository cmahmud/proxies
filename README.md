# SyndProxy private pool

## Current pool

- Alive now: 760
- Gold now: 406
- HTTP: 174 alive / 78 gold
- HTTPS: 157 alive / 21 gold
- SOCKS4: 220 alive / 150 gold
- SOCKS5: 209 alive / 157 gold

## Historical pool

- Discovered: 149514
- Ever alive: 26947
- Ever gold: 1089

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
