# SyndProxy private pool

## Current pool

- Alive now: 685
- Gold now: 377
- HTTP: 174 alive / 68 gold
- HTTPS: 109 alive / 19 gold
- SOCKS4: 194 alive / 136 gold
- SOCKS5: 208 alive / 154 gold

## Historical pool

- Discovered: 145577
- Ever alive: 25570
- Ever gold: 1066

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
