# SyndProxy private pool

## Current pool

- Alive now: 1907
- Gold now: 694
- HTTP: 745 alive / 233 gold
- HTTPS: 603 alive / 147 gold
- SOCKS4: 222 alive / 149 gold
- SOCKS5: 337 alive / 165 gold

## Historical pool

- Discovered: 142715
- Ever alive: 24461
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
