# SyndProxy private pool

## Current pool

- Alive now: 1158
- Gold now: 437
- HTTP: 403 alive / 110 gold
- HTTPS: 280 alive / 27 gold
- SOCKS4: 234 alive / 154 gold
- SOCKS5: 241 alive / 146 gold

## Historical pool

- Discovered: 160024
- Ever alive: 30562
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
