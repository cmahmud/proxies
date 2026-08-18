# SyndProxy private pool

## Current pool

- Alive now: 1066
- Gold now: 345
- HTTP: 387 alive / 48 gold
- HTTPS: 214 alive / 14 gold
- SOCKS4: 234 alive / 142 gold
- SOCKS5: 231 alive / 141 gold

## Historical pool

- Discovered: 107115
- Ever alive: 14856
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
