# SyndProxy private pool

## Current pool

- Alive now: 902
- Gold now: 405
- HTTP: 266 alive / 92 gold
- HTTPS: 182 alive / 18 gold
- SOCKS4: 219 alive / 151 gold
- SOCKS5: 235 alive / 144 gold

## Historical pool

- Discovered: 155696
- Ever alive: 29275
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
