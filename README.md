# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 343
- HTTP: 113 alive / 43 gold
- HTTPS: 97 alive / 9 gold
- SOCKS4: 164 alive / 151 gold
- SOCKS5: 179 alive / 140 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32797
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
