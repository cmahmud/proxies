# SyndProxy validated proxy pool

## Current pool

- Alive now: 443
- Gold now: 306
- HTTP: 128 alive / 74 gold
- HTTPS: 33 alive / 17 gold
- SOCKS4: 101 alive / 70 gold
- SOCKS5: 181 alive / 145 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47819
- Ever gold: 1482

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
