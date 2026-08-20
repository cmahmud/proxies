# SyndProxy private pool

## Current pool

- Alive now: 710
- Gold now: 390
- HTTP: 187 alive / 76 gold
- HTTPS: 118 alive / 20 gold
- SOCKS4: 194 alive / 140 gold
- SOCKS5: 211 alive / 154 gold

## Historical pool

- Discovered: 147183
- Ever alive: 25814
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
