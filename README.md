# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 390
- HTTP: 105 alive / 69 gold
- HTTPS: 37 alive / 15 gold
- SOCKS4: 159 alive / 151 gold
- SOCKS5: 181 alive / 155 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48220
- Ever gold: 1525

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
