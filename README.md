# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 400
- HTTP: 107 alive / 78 gold
- HTTPS: 35 alive / 17 gold
- SOCKS4: 167 alive / 151 gold
- SOCKS5: 177 alive / 154 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48235
- Ever gold: 1525

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
