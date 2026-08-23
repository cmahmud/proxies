# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 350
- HTTP: 97 alive / 37 gold
- HTTPS: 51 alive / 10 gold
- SOCKS4: 163 alive / 153 gold
- SOCKS5: 166 alive / 150 gold

## Historical pool

- Discovered: 171068
- Ever alive: 32858
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
