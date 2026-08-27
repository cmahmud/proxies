# SyndProxy validated proxy pool

## Current pool

- Alive now: 589
- Gold now: 419
- HTTP: 110 alive / 79 gold
- HTTPS: 124 alive / 18 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42074
- Ever gold: 1349

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
