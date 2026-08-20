# SyndProxy private pool

## Current pool

- Alive now: 844
- Gold now: 407
- HTTP: 217 alive / 84 gold
- HTTPS: 152 alive / 24 gold
- SOCKS4: 225 alive / 145 gold
- SOCKS5: 250 alive / 154 gold

## Historical pool

- Discovered: 151071
- Ever alive: 27448
- Ever gold: 1097

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
