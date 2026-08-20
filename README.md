# SyndProxy private pool

## Current pool

- Alive now: 1978
- Gold now: 656
- HTTP: 780 alive / 225 gold
- HTTPS: 634 alive / 121 gold
- SOCKS4: 245 alive / 145 gold
- SOCKS5: 319 alive / 165 gold

## Historical pool

- Discovered: 142698
- Ever alive: 24346
- Ever gold: 982

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
