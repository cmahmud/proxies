# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 385
- HTTP: 90 alive / 60 gold
- HTTPS: 37 alive / 11 gold
- SOCKS4: 176 alive / 156 gold
- SOCKS5: 177 alive / 158 gold

## Historical pool

- Discovered: 174823
- Ever alive: 33103
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
