# SyndProxy validated proxy pool

## Current pool

- Alive now: 463
- Gold now: 385
- HTTP: 93 alive / 60 gold
- HTTPS: 47 alive / 22 gold
- SOCKS4: 159 alive / 152 gold
- SOCKS5: 164 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43647
- Ever gold: 1375

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
