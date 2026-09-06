# SyndProxy validated proxy pool

## Current pool

- Alive now: 444
- Gold now: 358
- HTTP: 71 alive / 44 gold
- HTTPS: 29 alive / 9 gold
- SOCKS4: 169 alive / 154 gold
- SOCKS5: 175 alive / 151 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48300
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
