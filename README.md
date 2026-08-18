# SyndProxy private pool

## Current pool

- Alive now: 813
- Gold now: 286
- HTTP: 222 alive / 25 gold
- HTTPS: 143 alive / 5 gold
- SOCKS4: 227 alive / 144 gold
- SOCKS5: 221 alive / 112 gold

## Historical pool

- Discovered: 99165
- Ever alive: 12345
- Ever gold: 396

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
