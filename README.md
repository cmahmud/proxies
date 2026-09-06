# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 401
- HTTP: 113 alive / 78 gold
- HTTPS: 38 alive / 17 gold
- SOCKS4: 173 alive / 151 gold
- SOCKS5: 178 alive / 155 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48235
- Ever gold: 1525

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
