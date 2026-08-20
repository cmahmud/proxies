# SyndProxy private pool

## Current pool

- Alive now: 644
- Gold now: 364
- HTTP: 166 alive / 67 gold
- HTTPS: 105 alive / 23 gold
- SOCKS4: 181 alive / 129 gold
- SOCKS5: 192 alive / 145 gold

## Historical pool

- Discovered: 145579
- Ever alive: 25577
- Ever gold: 1066

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
