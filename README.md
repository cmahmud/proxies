# SyndProxy validated proxy pool

## Current pool

- Alive now: 445
- Gold now: 308
- HTTP: 158 alive / 79 gold
- HTTPS: 31 alive / 15 gold
- SOCKS4: 83 alive / 73 gold
- SOCKS5: 173 alive / 141 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47820
- Ever gold: 1492

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
