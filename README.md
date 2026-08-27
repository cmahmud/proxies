# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 418
- HTTP: 101 alive / 72 gold
- HTTPS: 117 alive / 20 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 183 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41928
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
