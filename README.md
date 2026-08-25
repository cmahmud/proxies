# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 421
- HTTP: 91 alive / 65 gold
- HTTPS: 88 alive / 25 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35642
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
