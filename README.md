# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 430
- HTTP: 129 alive / 77 gold
- HTTPS: 82 alive / 22 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 188 alive / 169 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33914
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
