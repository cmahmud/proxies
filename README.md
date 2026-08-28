# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 399
- HTTP: 110 alive / 75 gold
- HTTPS: 88 alive / 10 gold
- SOCKS4: 164 alive / 155 gold
- SOCKS5: 172 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43082
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
