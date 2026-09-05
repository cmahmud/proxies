# SyndProxy validated proxy pool

## Current pool

- Alive now: 438
- Gold now: 310
- HTTP: 128 alive / 74 gold
- HTTPS: 33 alive / 18 gold
- SOCKS4: 96 alive / 71 gold
- SOCKS5: 181 alive / 147 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47819
- Ever gold: 1484

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
