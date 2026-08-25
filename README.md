# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 404
- HTTP: 92 alive / 65 gold
- HTTPS: 72 alive / 20 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 176 alive / 158 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37717
- Ever gold: 1287

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
