# SyndProxy private pool

## Current pool

- Alive now: 1262
- Gold now: 443
- HTTP: 474 alive / 110 gold
- HTTPS: 298 alive / 33 gold
- SOCKS4: 227 alive / 137 gold
- SOCKS5: 263 alive / 163 gold

## Historical pool

- Discovered: 159266
- Ever alive: 30367
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
