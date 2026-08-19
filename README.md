# SyndProxy private pool

## Current pool

- Alive now: 1040
- Gold now: 524
- HTTP: 354 alive / 151 gold
- HTTPS: 266 alive / 105 gold
- SOCKS4: 222 alive / 143 gold
- SOCKS5: 198 alive / 125 gold

## Historical pool

- Discovered: 127372
- Ever alive: 19947
- Ever gold: 806

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
