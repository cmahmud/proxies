# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 395
- HTTP: 75 alive / 57 gold
- HTTPS: 79 alive / 14 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 176 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42866
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
