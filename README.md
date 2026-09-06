# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 395
- HTTP: 101 alive / 79 gold
- HTTPS: 32 alive / 16 gold
- SOCKS4: 163 alive / 150 gold
- SOCKS5: 178 alive / 150 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48235
- Ever gold: 1525

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
