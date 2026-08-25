# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 428
- HTTP: 101 alive / 70 gold
- HTTPS: 91 alive / 25 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 188 alive / 172 gold

## Historical pool

- Discovered: 183874
- Ever alive: 35726
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
