# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 399
- HTTP: 103 alive / 75 gold
- HTTPS: 40 alive / 16 gold
- SOCKS4: 171 alive / 151 gold
- SOCKS5: 180 alive / 157 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48227
- Ever gold: 1525

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
