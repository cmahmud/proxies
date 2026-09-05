# SyndProxy validated proxy pool

## Current pool

- Alive now: 451
- Gold now: 333
- HTTP: 109 alive / 76 gold
- HTTPS: 61 alive / 23 gold
- SOCKS4: 110 alive / 93 gold
- SOCKS5: 171 alive / 141 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47959
- Ever gold: 1505

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
