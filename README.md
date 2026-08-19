# SyndProxy private pool

## Current pool

- Alive now: 1108
- Gold now: 537
- HTTP: 395 alive / 162 gold
- HTTPS: 274 alive / 91 gold
- SOCKS4: 209 alive / 140 gold
- SOCKS5: 230 alive / 144 gold

## Historical pool

- Discovered: 122378
- Ever alive: 18609
- Ever gold: 721

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
