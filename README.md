# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 392
- HTTP: 100 alive / 74 gold
- HTTPS: 33 alive / 15 gold
- SOCKS4: 164 alive / 153 gold
- SOCKS5: 179 alive / 150 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48235
- Ever gold: 1525

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
