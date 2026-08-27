# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 398
- HTTP: 73 alive / 52 gold
- HTTPS: 47 alive / 17 gold
- SOCKS4: 173 alive / 164 gold
- SOCKS5: 181 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41589
- Ever gold: 1339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
