# SyndProxy private pool

## Current pool

- Alive now: 1059
- Gold now: 257
- HTTP: 427 alive / 31 gold
- HTTPS: 174 alive / 5 gold
- SOCKS4: 226 alive / 116 gold
- SOCKS5: 232 alive / 105 gold

## Historical pool

- Discovered: 95405
- Ever alive: 10987
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
