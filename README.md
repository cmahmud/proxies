# SyndProxy validated proxy pool

## Current pool

- Alive now: 672
- Gold now: 398
- HTTP: 145 alive / 79 gold
- HTTPS: 184 alive / 21 gold
- SOCKS4: 168 alive / 146 gold
- SOCKS5: 175 alive / 152 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39955
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
