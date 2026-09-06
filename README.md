# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 383
- HTTP: 95 alive / 64 gold
- HTTPS: 41 alive / 15 gold
- SOCKS4: 174 alive / 155 gold
- SOCKS5: 172 alive / 149 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48188
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
