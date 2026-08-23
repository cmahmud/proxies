# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 372
- HTTP: 89 alive / 56 gold
- HTTPS: 33 alive / 11 gold
- SOCKS4: 167 alive / 150 gold
- SOCKS5: 186 alive / 155 gold

## Historical pool

- Discovered: 174811
- Ever alive: 33099
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
