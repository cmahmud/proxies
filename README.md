# SyndProxy private pool

## Current pool

- Alive now: 1020
- Gold now: 423
- HTTP: 293 alive / 81 gold
- HTTPS: 226 alive / 26 gold
- SOCKS4: 221 alive / 142 gold
- SOCKS5: 280 alive / 174 gold

## Historical pool

- Discovered: 164960
- Ever alive: 32227
- Ever gold: 1176

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
