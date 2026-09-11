# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 426
- HTTP: 98 alive / 71 gold
- HTTPS: 59 alive / 25 gold
- SOCKS4: 195 alive / 169 gold
- SOCKS5: 182 alive / 161 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49088
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
