# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 384
- HTTP: 111 alive / 53 gold
- HTTPS: 43 alive / 10 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 183 alive / 162 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33476
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
