# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 390
- HTTP: 119 alive / 64 gold
- HTTPS: 59 alive / 13 gold
- SOCKS4: 166 alive / 151 gold
- SOCKS5: 185 alive / 162 gold

## Historical pool

- Discovered: 175451
- Ever alive: 33164
- Ever gold: 1228

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
