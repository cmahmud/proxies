# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 380
- HTTP: 119 alive / 44 gold
- HTTPS: 43 alive / 11 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 182 alive / 166 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33580
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
