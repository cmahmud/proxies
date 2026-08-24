# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 389
- HTTP: 95 alive / 55 gold
- HTTPS: 46 alive / 9 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 191 alive / 165 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33355
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
