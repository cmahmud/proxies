# SyndProxy private pool

## Current pool

- Alive now: 1079
- Gold now: 522
- HTTP: 377 alive / 161 gold
- HTTPS: 250 alive / 93 gold
- SOCKS4: 241 alive / 143 gold
- SOCKS5: 211 alive / 125 gold

## Historical pool

- Discovered: 123226
- Ever alive: 18927
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
