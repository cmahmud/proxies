# SyndProxy private pool

## Current pool

- Alive now: 1092
- Gold now: 544
- HTTP: 391 alive / 164 gold
- HTTPS: 250 alive / 94 gold
- SOCKS4: 239 alive / 145 gold
- SOCKS5: 212 alive / 141 gold

## Historical pool

- Discovered: 123170
- Ever alive: 18873
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
