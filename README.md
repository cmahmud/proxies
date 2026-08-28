# SyndProxy validated proxy pool

## Current pool

- Alive now: 465
- Gold now: 399
- HTTP: 78 alive / 56 gold
- HTTPS: 38 alive / 14 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 178 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42851
- Ever gold: 1363

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
