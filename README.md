# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 417
- HTTP: 137 alive / 70 gold
- HTTPS: 75 alive / 20 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33823
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
