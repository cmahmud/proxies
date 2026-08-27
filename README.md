# SyndProxy validated proxy pool

## Current pool

- Alive now: 605
- Gold now: 399
- HTTP: 87 alive / 59 gold
- HTTPS: 159 alive / 14 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 188 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41023
- Ever gold: 1316

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
