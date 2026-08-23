# SyndProxy validated proxy pool

## Current pool

- Alive now: 463
- Gold now: 375
- HTTP: 85 alive / 57 gold
- HTTPS: 37 alive / 11 gold
- SOCKS4: 163 alive / 151 gold
- SOCKS5: 178 alive / 156 gold

## Historical pool

- Discovered: 174811
- Ever alive: 33099
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
