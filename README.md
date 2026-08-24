# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 385
- HTTP: 111 alive / 53 gold
- HTTPS: 41 alive / 10 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 182 alive / 163 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33474
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
