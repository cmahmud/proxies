# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 298
- HTTP: 174 alive / 72 gold
- HTTPS: 40 alive / 23 gold
- SOCKS4: 205 alive / 68 gold
- SOCKS5: 209 alive / 135 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47801
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
