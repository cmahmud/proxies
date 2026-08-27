# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 406
- HTTP: 90 alive / 61 gold
- HTTPS: 83 alive / 16 gold
- SOCKS4: 186 alive / 163 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41558
- Ever gold: 1338

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
