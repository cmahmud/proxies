# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 380
- HTTP: 101 alive / 63 gold
- HTTPS: 40 alive / 13 gold
- SOCKS4: 177 alive / 151 gold
- SOCKS5: 181 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48114
- Ever gold: 1519

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
