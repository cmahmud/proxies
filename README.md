# SyndProxy validated proxy pool

## Current pool

- Alive now: 648
- Gold now: 444
- HTTP: 125 alive / 87 gold
- HTTPS: 138 alive / 23 gold
- SOCKS4: 185 alive / 163 gold
- SOCKS5: 200 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42226
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
