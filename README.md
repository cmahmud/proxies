# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 427
- HTTP: 102 alive / 70 gold
- HTTPS: 91 alive / 24 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 188 alive / 172 gold

## Historical pool

- Discovered: 183874
- Ever alive: 35727
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
