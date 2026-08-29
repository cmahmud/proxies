# SyndProxy validated proxy pool

## Current pool

- Alive now: 466
- Gold now: 386
- HTTP: 96 alive / 61 gold
- HTTPS: 47 alive / 22 gold
- SOCKS4: 160 alive / 151 gold
- SOCKS5: 163 alive / 152 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43647
- Ever gold: 1375

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
