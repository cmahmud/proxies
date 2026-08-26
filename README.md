# SyndProxy validated proxy pool

## Current pool

- Alive now: 671
- Gold now: 399
- HTTP: 144 alive / 79 gold
- HTTPS: 187 alive / 22 gold
- SOCKS4: 167 alive / 146 gold
- SOCKS5: 173 alive / 152 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39955
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
