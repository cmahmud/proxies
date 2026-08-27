# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 404
- HTTP: 91 alive / 63 gold
- HTTPS: 76 alive / 18 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 179 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41748
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
