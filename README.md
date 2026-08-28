# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 386
- HTTP: 84 alive / 65 gold
- HTTPS: 69 alive / 10 gold
- SOCKS4: 159 alive / 154 gold
- SOCKS5: 170 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43150
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
