# SyndProxy private pool

## Current pool

- Alive now: 990
- Gold now: 412
- HTTP: 299 alive / 87 gold
- HTTPS: 241 alive / 29 gold
- SOCKS4: 207 alive / 143 gold
- SOCKS5: 243 alive / 153 gold

## Historical pool

- Discovered: 164246
- Ever alive: 32081
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
