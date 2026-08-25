# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 416
- HTTP: 101 alive / 63 gold
- HTTPS: 85 alive / 20 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 186 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35532
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
