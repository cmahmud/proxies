# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 380
- HTTP: 123 alive / 71 gold
- HTTPS: 177 alive / 17 gold
- SOCKS4: 159 alive / 145 gold
- SOCKS5: 172 alive / 147 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39914
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
