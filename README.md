# SyndProxy private pool

## Current pool

- Alive now: 887
- Gold now: 402
- HTTP: 258 alive / 83 gold
- HTTPS: 202 alive / 25 gold
- SOCKS4: 212 alive / 149 gold
- SOCKS5: 215 alive / 145 gold

## Historical pool

- Discovered: 151072
- Ever alive: 27477
- Ever gold: 1097

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
