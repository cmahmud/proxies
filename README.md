# SyndProxy private pool

## Current pool

- Alive now: 843
- Gold now: 407
- HTTP: 217 alive / 84 gold
- HTTPS: 167 alive / 24 gold
- SOCKS4: 202 alive / 147 gold
- SOCKS5: 257 alive / 152 gold

## Historical pool

- Discovered: 151071
- Ever alive: 27434
- Ever gold: 1096

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
